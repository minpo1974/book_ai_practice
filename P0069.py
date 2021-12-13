
in_size = 2 #체중, 키
nb_classes = 6 #체형 6

from keras.models import Sequential
model = Sequential()

from keras.layers import Dense, Dropout
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.save('hw_model.h5')
print('saved')