import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.python.keras import metrics

iris_data = pd.read_csv("iris.csv", encoding="utf-8")

y_labels = iris_data.loc[:,"variety"]
x_data = iris_data.loc[:,["sepal.length","sepal.width","petal.length","petal.width"]]

#one-hot encoding

labels = {
    'Setosa':[1,0,0],
    'Versicolor' :[0,1,0],
    'Virginica' :[0,0,1]
}

def lambda_func(x) :
    return labels[x]
#print(labels["Setosa"])

#map(function, iterable)
#두번째 인자로 들어온 반복가능한 자료형(리스트,튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수 수행
y_nums = np.array(list(map(lambda v: labels[v], y_labels)))
x_data = np.array(x_data)
#print(x_data)

#map(lambda_func, y_labels)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_nums, train_size=0.8)

Dense = tf.keras.layers.Dense
model = tf.keras.models.Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(3, activation='softmax'))

model.compile(
    loss = 'categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
model.fit(x_train, y_train, batch_size=20, epochs=300)

score = model.evaluate(x_test, y_test, verbose=1)
print("정답률=", score[1], "loss=", score[0])

yhat = model.predict([[5.6, 2.9, 3.6, 1.3]])
print(yhat)