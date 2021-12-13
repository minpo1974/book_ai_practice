import tensorflow as tf
from tensorflow.keras.datasets import mnist
from matplotlib import pyplot
from tensorflow.python.keras.layers.core import Dropout
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D,MaxPooling2D
from tensorflow.keras.layers import Flatten

im_rows=28
im_cols=28
im_color=1
in_shape = (im_rows, im_cols, im_color)
out_size =10

(x_train, y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train.reshape(-1,im_rows,im_cols,im_color)
x_train = x_train.astype('float32')/255
x_test = x_test.reshape(-1,im_rows,im_cols,im_color)
x_test = x_test.astype('float32')/255

y_train = tf.keras.utils.to_categorical(y_train.astype('int32'),10)
y_test = tf.keras.utils.to_categorical(y_test.astype('int32'),10)

model = tf.keras.models.Sequential()
Dense = tf.keras.layers.Dense

model.add(
    Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=in_shape)
)
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(out_size, activation='softmax'))

model.compile(
    loss ='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

hist = model.fit(x_train, y_train, batch_size=128, epochs=20, verbose=1, validation_data=(x_test, y_test)) #epochs=50

score = model.evaluate(x_test,y_test,verbose=1)
print("정답률=", score[1], 'loss=', score[0])


plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy')
plt.legend(['train','test'], loc='upper left')
plt.show()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss')
plt.legend(['train','test'], loc='upper left')
plt.show()