#데이터 읽어들이기
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Activation, Flatten

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

#데이터 정규화
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255

import tensorflow as tf

#one-hot
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)

#모델 정의
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import Conv2D, MaxPooling2D

im_rows=32
im_cols=32
in_shape=(im_rows,im_cols,3)

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

#학습
hist = model.fit(
    x_train, y_train,
    batch_size=32, epochs=50,
    verbose=1,
    validation_data=(x_test,y_test)
)

#가중치 저장
model.save_weights('cifar10-wight.h5')

#가중치 읽기
#model.load_weights('cifar10-weight.h5')

#모델 평가
score = model.evaluate(x_test, y_test, verbose=1)
print('정답률=',score[1], 'loss=',score[0])

#학습상태 그리기
#학습 상태 그래프
import matplotlib.pyplot as plt
plt.plot(hist.history['accuracy']) #훈련 정확도, 1에 가깝고 높을 수록 좋은 모델
plt.plot(hist.history['val_accuracy']) #검증 정확도
plt.title('Accuracy')
plt.legend(['train','test'], loc='upper left')
plt.show()
plt.plot(hist.history['loss']) #훈련 손실값, 결과 값과의 차이, 작을 수록 좋고.. 0에 수렴할 수록 좋은 모델
plt.plot(hist.history['val_loss']) #검증 손실값
plt.title('Loss')
plt.legend(['train','test'],loc='upper left')
plt.show()