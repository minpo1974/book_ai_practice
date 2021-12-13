import os.path
import re
import glob
import json
from sklearn import svm
from sklearn import metrics
import sklearn

#텍스트를 읽어들이고 출현 빈도 조사
def check_freq(fname) :
    name = os.path.basename(fname)
    #print(name)
    #a{2,}b 는 'aab', 'aaaaaaaaaaaaaaaab',ab(x)
    #^d와 $는 기본적으로 행 시작, 행 끝
    lang = re.match(r'^[a-z]{2,}', name).group()
    #print("lang :", lang)
    with open(fname, "r", encoding="utf-8") as f :
        text = f.read()
    text = text.lower()
    cnt = [ 0 for n in range(0, 26)]
    #print(cnt)
    code_a = ord("a")
    code_z = ord("z")

    #알파벳 출현 횟수
    for ch in text :
        n = ord(ch)
        if code_a <= n <= code_z :
            cnt[n - code_a] += 1
    #print("cnt: ", cnt)
    total = sum(cnt)
    #print(total)
    freq = list(map(lambda n : n/total , cnt))
    #print("freq : ", freq)
    return (freq, lang)

def load_files(path) :
    freqs = []
    labels = []
    file_list = glob.glob(path)
    #print(file_list)    
    for fname in file_list :
        r = check_freq(fname)
        #print("r[0] : ", r[0])
        #print("r[1] : ", r[1])
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

data = load_files("./lang/train/*.txt")
#print("data : ", data)
test = load_files("./lang/test/*.txt")
#print("test : ", test)

#JSON 으로 저장
with open("./lang/freq.json", "w", encoding="utf-8") as fp :
    json.dump([data, test], fp)

#학습하기
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

#예측
predict = clf.predict(test["freqs"])

#결과 테스트

from sklearn.metrics import confusion_matrix

ac_score = metrics.accuracy_score(test["labels"], predict)

conf_mat = confusion_matrix(test["labels"], predict)

print("Confusion matrix:\n", conf_mat)

cl_report = metrics.classification_report(test["labels"], predict)
print("정답률=", ac_score)
print("Report=")
print(cl_report)

print("-----------------------------")

#y_true = [2,0,2,2,0,1]
#y_pred = [0,0,2,2,0,2]

y_true = [1,1,0,1,0,0,1,0,0,0]
y_pred = [1,0,0,1,0,0,1,1,1,0]

'''   0 1 (predicted)
 0  [[4 2]
 1   [1 3]]
(expected)
            암예측  암아님예측
실제로암      [TP      FN]
실제로암아님  [FP      TN]
TP : True Positive : 암을 암이라고 정확하게 예측, 양성예측
TN : True Negative : 암이 아닌 것을 암이 아니라고 예측, 음성예측
FP : False Positive : 암이 아닌 것을 암이라고 예측
FN : False Negative : 암인데 암이 아니라고 예측

[[2 0 0]
 [0 0 1]
 [1 0 2]]

 [TP  FP/FN  FP/FN]
 [FP/FN  TP  FP/FN]
 [FP/FN  FP/FN  TP]



Accuracy(정확도) : 전체 샘플 중 맞게 예측한 샘플 수
높을 수록 좋다.
accuracy = (TP+TN)/(TP+FN+FP+TN)

Precision(정밀도) : 양성 클래스에 속한다고 출력한 샘플 중 실제로 양성 클래스에 속하는 샘플 수
높을 수록 좋은 모형
예) 실제 암이라고 판단한 것 중에 실제 암의 비율
precision = TP/(TP+FP)

Recall(재현율) : 실제 양성 클래스에 속한 표본 중에 양성 클래스에 속한다고 출력한 표본의 수의 비율
높을 수록 좋은 모형
예) 실제 암 중에서 실제 암이라고 예측한 비율
TPR(True Positive rate), Sensitivity
recall = TP/(TP+FN)

암예측  암아님예측
실제로암      [TP      FN]
실제로암아님  [FP      TN]

위양성율(fall-out) : 실제 양성 클래스에 속하지 않는 표본 중에 양성 클래스에 속한다고 추력한 표본의 비율
낮을 수록 좋다
fallout = FP/(FP+TN)

f-score : 정밀도(precision)와 재현률(recall)의 weight harmonic average(가중조화평균)
정밀도에 주어진 가중치를 베타(beta)
beta가 1인경우, F1
F1 = 2*precision*recall/(precision+recall)

metrics package에서 정밀도, 재현율, F1 점수를 구하는 classification_report 명령

           precision    recall  f1-score   support

     class 0       0.75      0.60      0.67         5
     class 1       0.33      0.50      0.40         2

    accuracy                           0.57         7
   macro avg       0.54      0.55      0.53         7
weighted avg       0.63      0.57      0.59         7

macro avg : 단순평균
weighted avg : 각 클래스에 속하는 표본의 갯수로 가중평균
accuracy : 정확도, 전체 학습데이터의 개수에서 각 클래스에서 자신의 클래스를 정확하게 맞춘 개수의 비율

'''
conf_mat = confusion_matrix(y_true, y_pred)
print("shape : ", conf_mat.shape)
print("confusion matrix : \n", conf_mat)

y_true = [0, 0, 1, 1, 2, 2, 2]
y_pred = [0, 0, 1, 2, 2, 2, 1]
target_names = ['class 0', 'class 1', 'class 2']
print(metrics.classification_report(y_true, y_pred, target_names=target_names))
