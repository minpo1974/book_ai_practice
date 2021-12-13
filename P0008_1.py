#wine 품질 판정하기
import pandas as pd

wine = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8" )

#quality에 대한 data만 y 종속변수에 넣는다.(결과)
y = wine["quality"]
print(y)

#x는 'quality' 종속 변수를 제외한 나머지를 x에 지정한다.(입력데이터)
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

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#모델 생성
from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier(max_depth=5)
from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier(n_estimators=200)
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression(max_iter=1000)

#모델 학습
DT.fit(x_train,y_train)
RFC.fit(x_train,y_train)
LR.fit(x_train,y_train)

#예측과 평가
predict_DT = DT.predict(x_test)
predict_RFC = RFC.predict(x_test)
predict_LR = LR.predict(x_test)

from sklearn.metrics import accuracy_score,confusion_matrix, recall_score, precision_score,f1_score
def print_Metric(y, pred_y, title=None) :
    print(title)
    print("Accuracy : ", accuracy_score(y,pred_y))
    print("Recall : ", recall_score(y,pred_y, average='micro'))
    print("Precision : ", precision_score(y,pred_y, average='micro'))
    print("F1 Score : ", f1_score(y,pred_y, average='micro'))

#confusion matrix 결과
print('===============')
print('Dicistion Tree Result')
print(confusion_matrix(y_test, predict_DT))
print_Metric(y_test,predict_DT,'Dicistion Tree Result')
print('RandomForest Result')
print(confusion_matrix(y_test, predict_RFC))
print_Metric(y_test,predict_RFC,'RandomForest Result')
print('Logistic Regression Result')
print(confusion_matrix(y_test, predict_LR))
print_Metric(y_test,predict_LR,'Logistic Regression Result')
print('===============')
