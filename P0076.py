from itertools import accumulate
from keras import activations, models
from keras.layers.core import Dropout
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from numpy.core.numeric import tensordot
from tensorflow.python.ops.gen_batch_ops import batch

def def_model(in_shape, nb_classes) :
    model = Sequential()
    model.add(
        Conv2D(
            32,
            kernel_size=(3,3),
            activation='relu',
            input_shape = in_shape
        )
    )
    model.add(Conv2D(32,(3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64,(3,3), activation='relu'))
    model.add(Conv2D(64,(3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes, activation='softmax'))

    return model

def get_model(in_shape, nb_classes) :
    model = def_model(in_shape, nb_classes)
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    return model

im_rows = 32
im_cols = 32
im_color = 3
in_shape = (im_rows, im_cols, im_color)
nb_classes = 3 #3가지 종류의 음식

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

photos = np.load('image1/photos1.npz')
x = photos['x']
y = photos['y']

x = x.reshape(-1, im_rows, im_cols, im_color)
x = x.astype('float32') /255

y = tf.keras.utils.to_categorical(y.astype('int32'), nb_classes)

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8)

model = get_model(in_shape, nb_classes)

hist = model.fit(x_train, y_train, batch_size=32, epochs=20, verbose=1, validation_data=(x_test,y_test))

score= model.evaluate(x_test, y_test, verbose=1)
print('정답률=', score[1], '손실률=', score[0])

import matplotlib.pyplot as plt

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

model.save_weights('./image1/photos-model-light.hd5')