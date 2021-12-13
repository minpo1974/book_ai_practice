import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten

im_rows = 32
im_cols = 32
in_shape = (im_rows, im_cols, 3)

model = Sequential()
model.add(Conv2D(32,(3,3), padding='same', input_shape=in_shape))
model.add(Activation('relu'))
model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

#모델 컴파일
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.load_weights('cifar10-wight.h5')

#OpenCV를 사용해서 이미지를 읽어
import cv2
im = cv2.imread('test-car.jpg')

#색공간변화, 크기조절
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
im = cv2.resize(im,(32,32))

import matplotlib.pyplot as plt

plt.imshow(im)
plt.show()

#예측
import numpy as np
r = model.predict(np.array([im]), batch_size=32, verbose=1)
res = r[0]

#결과출력
labels = ["airplane", "automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

for i, acc in enumerate(res) :
    print(labels[i], "=", int(acc*100))

print("----")
print("예측한 결과=", labels[res.argmax()])
