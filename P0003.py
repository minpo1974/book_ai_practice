import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#Iris 데이터를 utf-8 형식으로 읽어들인다.
#엑셀 데이터 저장 방식에 따라, encoding 형식을 결정한다.
irisData = pd.read_csv('d:/test/iris.csv', encoding='utf-8')
#csv data를 출력해본다.
print(irisData)

#Iris 데이터를 레이블과 입력 데이터로 분리
y = irisData.loc[:, "variety"]
x = irisData.loc[:, ["sepal.length","sepal.width","petal.length","petal.width"]]

#머신러닝 모델을 학습하고 그 결과를 검증하기 위해서는
#원본 데이터를 Training(학습), Validation(검증), Testing(테스트)의 용도로 분리한다.
#학습데이터를 100%로 학습시킨 후, test 데이터에 모델을 적용했을 때 성능이 거의 나오지 않는다.
#이 현상을 Overfitting 되었다라고 한다.
#모델이 학습할 데이터에 과적합되도록 학습하여, 조금이라도 벗어난 데이터에 대해서는 예측율이 많이 떨어진다.
#일반적으로 train과 test 데이터셋으로 구분되어 있던 것을
#train에서 train(학습)/validation(검증)으로 일정 비율로 분리한 다음,
#학습할 때, train 데이터셋으로 학습 후, validation 데이터셋으로
#학습한 모델을 평가해준다.
#Machine Learning Model의 Hyper-Parameter를 값을 조정할 때,
#n_estimators 값으로 validation 데이터셋의 오차율을 점검해 나간다.
#Deep Learning Model도 validation_data를 지정하여,
#epoch마다 validation 오차율을 확인하면서 overfitting을 방지한다.
#모델이 overfitting이 되었다면, validation 데이터셋으로 검증시,
#예측율이나 오차율이 떨어지는 현상을 확인할 수 있다.
#Overfitting이 발생하면, 일반적으로 학습을 종료한다.

#scikit-learn 패키지 중 model_selection에는 데이터 분할을 위한 
#train_test_split 함수를 이용한다.
#train_test_split(arrays,test_size,train_size,random_state,shuffle,stratify)
#  - arrays:분할시킬 데이터를 입력 (파이썬list, 넘파이array, 판다스dataframe 등)
#  - test_size:테스트 데이터셋의 비율(float) 또는 개수(int)(default=0.25)
#              주로, test_size값을 지정해준다.
#  - train_size:학습 데이터셋의 비율(float) 또는 개수(int)(default=test_size의 나머지)
#  - random_state:데이터를 분할할 때, 셔플 발생의 시드값 (int나 RandomState로 입력)
#              parameter 튜닝시, 이 값을 고정해두고 튜닝해야
#              매번, 데이터셋이 변경되는 것을 방지할 수 있다.
#  - shuffle : 셔플 여부 설정 (default=True), 보통은 default로 둔다.
#              데이터를 쪼개기 전에, 데이터를 shuffing 할지의 여부이다.
#  - stratify : data의 비율 유지, default 값은 None이다.
#    classification에서 매우 중요한 옵션값,
#    예를 들어, label 집합인 y가 0(25%)과 1(75%)이 있을 때,
#    stratify=Y로 설정하면 나누어진 데이터셋들도
#    0과 1을 각각 25%, 75%로 유지한 채 분할된다.
#    값을 target으로 지정하면, 각각의 class 비율 train과 validation에 유지해준다
#    만약, target을 지정하지 않고 classification 문제를 다루면,
#    성능의 차이가 많이 날 수 있다. 반드시 확인해보길 바란다.
# Return 값 : 
#  - x_train, x_test, y_train, y_test : arrays에 data와 label을 둘 다 넣었을 경우의 return 값, 데이터와 레이블의 순서쌍은 유지
#  - x_train, x_test : arrays에 label 없이 data만 넣었을 경우의 return

#학습 데이터와 테스트 데이터로 분리한다.
#테스트 데이터는 0.2 즉, 20%의 데이터이다.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

#학습하기
#SVM(Support Vector Machine)
#주어진 데이터가 어느 그룹에 속하는지 분류하는 분류 모델
#두 부류 사이에 존재하는 여백을 의미하는 마진(margin)을 최대화 노력
#마진(margin) : 분류선(Dictionary Boundary)과 가장 가까운 데이터들과의 거리
#SVC(kernel, C) : kernel은 데이터셋을 분류할 커널 방식을 의미하고 C는 마진과 관련있다.
#마진 값이 작더라도 데이터셋을 정확히 분류하길 원하면 C값을 크게 주면 된다.
#데이터를 일부 오분류하더라도 최대한 마진을 크게 잡고 싶다면 C값을 작게 주면 된다.

clf = SVC() #SVM 알고리즘
clf.fit(x_train, y_train) # 학습을 하는 함수

#테스트 데이터로 예측해보기
#예측 결과를 리스트 형태로 받는다.
y_pred = clf.predict(x_test)
print("Accuracy(정답률)=", accuracy_score(y_test, y_pred))

print(clf.classes_)
print('the true label:',y_train[:20])
print('the predict label:', clf.predict(x_train)[:20])