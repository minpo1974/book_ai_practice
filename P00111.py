image_w = 28
image_h = 28
nb_classes = 10

from P00108 import build_model
from keras.datasets import mnist
from keras.layers.core import Activation, Dropout
from keras.utils import np_utils
from sklearn.model_selection import train_test_split

import numpy as np

def main() :
    #(x_train, y_train), (x_test, y_test) = mnist.load_data()
    xy = np.load("./image/font_draw1.npz")
    X = xy["x"]
    Y = xy["y"]

    X = X.reshape(X.shape[0], image_w*image_h).astype('float32')
    X /= 255
    Y = np_utils.to_categorical(Y, 10)

    x_train, x_test, y_train, y_test = train_test_split(X, Y)

    model = build_model()
    model.fit(x_train, y_train,
            batch_size=128, epochs=20, verbose=1,
            validation_data=(x_test,y_test)
    )
    model.save_weights('font_draw1.hdf5')
    score=model.evaluate(x_test,y_test, verbose=0)
    print('score=', score)

from keras.models import Sequential
from keras.layers import Dense

def build_model() :
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
        optimizer='rmsprop',
        metrics=['accuracy'])
    return model
    

if __name__ == '__main__' :
    main()