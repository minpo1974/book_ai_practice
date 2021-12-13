import tensorflow as tf
from tensorflow.keras.datasets import cifar10

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

#데이터 읽어들이기
from tensorflow.keras.datasets import cifar10
(x_train,y_train),(x_test,y_test) = cifar10.load_data()

im_rows=32
im_cols=32
im_size = im_rows*im_cols*3
#print(x_train.shape)
#print(x_train.ndim)
x_train = x_train.reshape(-1,im_size).astype('float32')/255
x_test = x_test.reshape(-1,im_size).astype('float32')/255
#print(x_train.shape)
#print(x_train.ndim)

#one-hot
import tensorflow as tf

y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)
#print(y_train[0])

#모델 정의
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(im_size,)))
model.add(Dense(10, activation='softmax'))

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

#평가
score = model.evaluate(x_test,y_test,verbose=1)
print('정답률=',score[1], 'loss=',score[0])

#학습상태 그래프
import matplotlib.pyplot as plt

plt.plot(hist.history['accuracy']) #훈련정확도, 1에 가깝고 높을 수록 좋은 모델
plt.plot(hist.history['val_accuracy']) #검증 정확도
plt.title('Accuracy')
plt.legend(['train','test'],loc='upper left')
plt.show()

plt.plot(hist.history['loss']) #훈련손실값, 결과값과의 차이, 작을수록 좋고..0에 수렴할 수록 좋은 모델
plt.plot(hist.history['val_loss']) #검증 손실값
plt.title('Loss')
plt.legend(['train','test'],loc='upper left')
plt.show()

#epoch의 횟수가 많아질수록 losss는 줄어든다. accuracy는 증가, 어느시점에 성능이 떨어지면.. 오버피팅