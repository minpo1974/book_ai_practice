#wine 품질 판정하기
import pandas as pd

#와인 데이터(cvs)를 읽어온다.
wine = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8" )

#quality에 대한 data만 y 종속변수에 넣는다.(결과)
y = wine["quality"]
print(y)

#x는 'quality' 종속 변수를 제외한 나머지를 x에 지정한다.(입력데이터)
#drop()함수에 index, column이라는 파라미터를 사용하지 않는다면
#axis=0 또는 axis=1 파라미터값을 넣어야 한다.
#axis = 0은 dataframe 행 단위를 수정할 때 필요한 파라미터 값이다.
#axis = 1은 dataframe 열 단위를 수정할 때 필요한 파라미터 값이다.

x = wine.drop("quality", axis=1) #'quality'열 삭제
print(x)

#quality에 대해, 0~4까지는 0, 5~7까지는 1, 8이상은 2 값으로 재조정한다.
newlist = []
for v in list(y) :
    if v <= 4 :
        newlist += [0]
    elif v <=7 :
        newlist += [1]
    else :
        newlist += [2]

y = newlist
print('0의 개수', y.count(0))
print('1의 개수', y.count(1))
print('2의 개수', y.count(2))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# RandomForest는 여러 개의 결정트리(Decision Tree)를 활용한 배깅 방식의 대표적인 알고리즘
# 배깅(Bagging)은 Bootstrap Aggregating의 약자로, 보팅(Voting)과는 달리 동일한 알고리즘으로 여러 분류기를 만들어 보팅으로 최종 결정하는 알고리즘

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
'''
Precision:- Accuracy of positive predictions.
Precision = TP/(TP + FP)

Recall:- Fraction of positives that were correctly identified.
Recall = TP/(TP+FN)

F1 score
F1 Score = 2*(Recall * Precision) / (Recall + Precision)

Accuracy : (TP+TN) / all
macro avg = (normal+abnormal) /2 * precision or recall or f1 score
weighted avg = normal/(normal+abnormal)  *  precision or recall or f1 score
'''
'''
y_test : 정답지
y_pred : 예측값
'''

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
print('랜덤 포레스트 정확도: {:.4f}'.format(accuracy))
