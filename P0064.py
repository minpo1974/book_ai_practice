from sklearn import datasets
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout

iris = datasets.load_iris()

in_size = 4
nb_classes = 3

x = iris.data
y = tf.keras.utils.to_categorical(iris.target, nb_classes)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(nb_classes, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.fit(x,y,batch_size=20,epochs=50)
model.save('iris_model.h5')
model.save_weights('iris_weight.h5')

print("ok")
