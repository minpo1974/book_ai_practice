from sklearn.linear_model import LinearRegression
#데이터를 불러올 때 필요
import pandas as pd
#배열을 변경할 때 필요
import numpy as np
#데이터의 시각화를 위해 필요
import matplotlib.pyplot as plt

df = pd.read_csv("height.csv")
#데이터의 일부를 출력(default : 5개)
print(df.head())

#몸무게 데이터
X = df["height"]
#키 데이터
y = df["weight"]
plt.plot(X, y, '*')

plt.show()

line_fitter = LinearRegression()
line_fitter.fit(X.values.reshape(-1,1), y)

#몸무게 80인 사람의 키를 예측
print("몸무게 80인 사람의 키는?")
print(line_fitter.predict([[80]]))

#기울기는?
print("기울기는?")
print(line_fitter.coef_)
#절편은?
print("절편은?")
print(line_fitter.intercept_)

#기존의 X값으로 y를 예측한 그래프
plt.plot(X, y, '*')
plt.plot(X,line_fitter.predict(X.values.reshape(-1,1)))
plt.show()