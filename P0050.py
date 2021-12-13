import tensorflow as tf
from tensorflow.keras.datasets import mnist
from matplotlib import pyplot
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

for i in range(0, 32) :
    pyplot.subplot(4,8,i+1)
    pyplot.imshow(x_train[i], cmap='gray')

#pyplot.show()
#print(x_train)

x_train = x_train.reshape(-1, 784).astype('float32') / 255
x_test = x_test.reshape(-1, 784).astype('float32') /255

#print(x_train[0])

y_train = tf.keras.utils.to_categorical(y_train.astype('int32'))
y_test = tf.keras.utils.to_categorical(y_test.astype('int32'))

#print(y_train[0])
#print(y_test[0])
in_size = 28*28
out_size = 10

Dense = tf.keras.layers.Dense
model = tf.keras.models.Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dense(out_size, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.fit(x_train,y_train, batch_size=20, epochs=1)
score=model.evaluate(x_test,y_test, verbose=1)
print("정답률=", score[1], 'loss=', score[0])

n = 0
plt.imshow(x_test[n].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()

