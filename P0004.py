import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

iris_data = pd.read_csv('d:/test/iris.csv', encoding='utf-8')

y = iris_data.loc[:, "variety"]
x = iris_data.loc[:, ["sepal.length","sepal.width","petal.length","petal.width"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

#SVM(Support Vector Machine)
#주어진 데이터가 어느 그룹에 속하는지 분류하는 분류 모델
#두 부류 사이에 존재하는 여백을 의미하는 마진(margin)을 최대화 노력
#마진(margin) : 분류선(Dictionary Boundary)과 가장 가까운 데이터들과의 거리
#SVC(kernel, C) : kernel은 데이터셋을 분류할 커널 방식을 의미하고 C는 마진과 관련있다.
#마진 값이 작더라도 데이터셋을 정확히 분류하길 원하면 C값을 크게 주면 된다.
#데이터를 일부 오분류하더라도 최대한 마진을 크게 잡고 싶다면 C값을 작게 주면 된다.

import numpy as np

mx=0
mxi=0

#최적의 C값을 찾아내는 코드입니다.
for i in np.arange(0.1,5.0,0.1): #0.1부터 5.0이전까지, 0.1씩 증가
    print('C=',i, ', kernel=', 'linear')
    clf = SVC(kernel='linear',C=i)
    clf.fit(x_train, y_train)

    print()
    print("학습 데이터 측정 정확도=%.2f" % clf.score(x_train, y_train))
    print("시험 데이터 측정 정확도=%.2f" % clf.score(x_test, y_test))
    
    if clf.score(x_test, y_test)>mx:
        mx=clf.score(x_test, y_test)
        mxi=i

print('시험 데이터 측정 최대치 : ', mx, ', 해당 C 값 =%.2f' %mxi)

