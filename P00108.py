image_w = 28
image_h = 28
nb_classes = 10

from keras.datasets import mnist
from keras.engine import input_layer
from keras.layers.core import Activation, Dropout
from keras.utils import np_utils

def main() :
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #print(x_train.shape)
    #print(x_train.shape[0])
    x_train = x_train.reshape(x_train.shape[0], image_w*image_h).astype('float32')
    #print(x_test.shape)
    #print(x_test.shape[0])
    x_test = x_test.reshape(x_test.shape[0], image_w*image_h).astype('float32')
    #print(x_train[0])
    x_train /= 255
    x_test /= 255
    #print(x_train[0])
    y_train = np_utils.to_categorical(y_train, nb_classes)
    y_test = np_utils.to_categorical(y_test, nb_classes)
    #print(y_test)
    model = build_model()
    model.fit(x_train, y_train,
        batch_size=128, epochs = 20, verbose=1,
        validation_data=(x_test,y_test)
    )
    model.save_weights('mnist_1.hdf5')
    score = model.evaluate(x_test, y_test, verbose=0)
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
