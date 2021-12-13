#root_dir = "./image"
root_dir = "D:/test/httpd-2.4.48-win64-VS16/Apache24/htdocs/image"
categories = ["normal","beni","negi","cheese"]
nb_classes = len(categories)
image_size = 50

import numpy as np
from tensorflow.keras import utils

def main() :
    x_train, x_test, y_train, y_test = np.load("./image/gyudon1.npy", allow_pickle=True)
    x_train = x_train.astype("float") / 256
    x_test = x_test.astype("float") / 256
    #print(y_train)
    y_train = utils.to_categorical(y_train, nb_classes)
    y_test = utils.to_categorical(y_test, nb_classes)
    #print(y_train)
    model = model_train(x_train, y_train)
    model_eval(model, x_test, y_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense

def model_eval(model, x, y) :
    score = model.evaluate(x, y)
    print('loss=', score[0])
    print('accuracy=',score[1])

def build_model(in_shape) :
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, padding='same', input_shape=in_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Convolution2D(64, 3, 3, padding='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(Dropout(0.25))
    model.add(Flatten()) 
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='binary_crossentropy',   optimizer='rmsprop',   metrics=['accuracy'])
    return model

def model_train(x, y) :
    model = build_model(x.shape[1:])
    model.fit(x,y, batch_size=32, epochs=30)
    hd5_file = "./image/gyudon-model2.hdf5"
    model.save_weights(hd5_file)
    return model

if __name__ == "__main__" :
    main()