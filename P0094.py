caltech_dir = "./caltechimage/101_ObjectCategories"
categories = ["chair","camera","butterfly","elephant", "flamingo"]
nb_classes = len(categories)

image_w = 64
image_h = 64
pixels = image_w * image_h * 3

import numpy as np

## 먼저 기존의 np.load를 np_load_old에 저장해둠.
np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
x_train, x_test, y_train, y_test = np.load("./5obj_1.npy")
np.load = np_load_old

#print(x_test)
x_train = x_train.astype("float") / 256
x_test = x_test.astype("float") / 256
#print(x_test)
#print(x_train.shape)
#print(x_test.shape)

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPool2D
from keras.layers import Activation, Dropout, Flatten, Dense

#keras를 통해 딥러닝 모델을 만들기 위해 층을 쌓을 준비가 되었다..
model = Sequential()

'''
이미지 데이터의 합성곱층 만들기
첫번째 : 필터의 수 만큼 데이터를 출력
두번째 : 필터의 크기를 지정, 3x3, 이미지를 반목해서 검사, 특징을 찾아낸다.
세번째 : valid, same

'''
#model.add(Convolution2D(32, (3,3), border_mode='same', input_shape=x_train.shape[1:]))
model.add(Convolution2D(32, (3,3), padding='same', input_shape=x_train.shape[1:]))
'''
Activation은 활성화 함수를 사용할 수 있게 해준다.
relu, softmax, sigmoid 등
'''
model.add(Activation('relu'))
'''
maxpooling은 이미지의 사소한 특징들을 무시한다.
2x2, 가장 높은 값을 모아서 출력 이미지를 정한다.
2x2, 원래의 이미지의 1/2이 된다.
'''
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64,(3,3)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

'''
Fully Connected Network에 전달해주어야 하는데... 1차원 데이터를 전달해야 한다.
현재 사용하고 있는 것은 2차원 데이터..=> 1차원 데이터로 변경
'''
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

'''
loss : 손실, 가중치 세트를 평가
optimizer : 가중치를 최적화, adam, rmprop
metrics : 평가척도.. 분류문제. accuracy
'''
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

'''
첫인자 : 학습할 데이터
두번째인자 : 학습할 데이터의 답
batch_size : 여러개의 작은 배체로 나누어서 매개변수를 조정
epochs : 반복 학습 수
'''
model.fit(x_train, y_train, batch_size=32, epochs=50)

score = model.evaluate(x_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])
