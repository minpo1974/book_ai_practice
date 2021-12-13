# 카테고리 지정하기
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)
# 이미지 크기 지정하기
image_w = 64 
image_h = 64

import numpy as np
from tensorflow.python.ops.gen_array_ops import prevent_gradient

## 먼저 기존의 np.load를 np_load_old에 저장해둠.
np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
x_train, x_test, y_train, y_test = np.load("./5obj_1.npy")
np.load = np_load_old

# 데이터 정규화하기
x_train = x_train.astype("float") / 256
x_test  = x_test.astype("float")  / 256

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPool2D
from keras.layers import Activation, Dropout, Flatten, Dense

model = Sequential() 
model.add(Convolution2D(32,(3,3),padding='same',input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64,(3,3)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

import os

hdf5_file = "./5obj-model_1.hdf5"
if os.path.exists(hdf5_file) :
    model.load_weights(hdf5_file)
else :
    model.fit(x_train, y_train, batch_size=32, epochs=50)
    model.save_weights(hdf5_file)

pre = model.predict(x_test)

from PIL import Image

errorpage = "./caltechimage/error/"
if not os.path.exists(errorpage) :
    os.mkdir(errorpage)
    
for i, v in enumerate(pre) :
    #print(i)
    #print(v)
    pre_ans = v.argmax() #예측한 레이블
    #print(pre_ans)
    #print(categories[pre_ans])
    ans = y_test[i].argmax() #정답레이블
    data = x_test[i] #이미지 데이터
    if pre_ans == ans : continue
    #예측이 틀리면, 무엇이 틀렸는지 출력
    print("[NG]", categories[pre_ans], "!=", categories[ans])
    #print(v)
    fname = "./caltechimage/error/" + str(i) +"-" + categories[pre_ans]+"-ne-"+categories[ans]+".png"
    #print(fname)
    data *= 256    
    img = Image.fromarray(np.uint8(data))
    img.save(fname)