from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dense

def def_model(in_shape, nb_classes) :
    model = Sequential()
    model.add(
        Conv2D(
            32,
            kernel_size=(3,3),
            activation='relu',
            input_shape=in_shape
        )
    )
    model.add(Conv2D(32, (3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3,3), activation='relu'))
    model.add(Conv2D(64, (3,3), activation='relu'))
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

import numpy as np

im_rows = 32
im_cols = 32
im_color = 3
in_shape = (im_rows, im_cols, im_color)
nb_classes = 3

labels = ["초밥", "샐러드", "마파두부"]
calories = [588, 118, 648]

model = get_model(in_shape, nb_classes)
model.load_weights('./image1/photos-model-light.hd5')

from PIL import Image
import matplotlib.pyplot as plt

def check_photo(path) :
    img = Image.open(path)
    img = img.convert("RGB")
    img = img.resize((im_cols, im_rows))
    plt.imshow(img)
    plt.show()
    x = np.asarray(img)
    x = x.reshape(-1, im_rows, im_cols, im_color)
    x = x.astype('float32')/ 255

    pre = model.predict([x])[0]
    print("pre : ", pre)
    idx = pre.argmax()
    print("idx : ", idx)
    per = int(pre[idx]*100)
    print(per)
    return (idx, per)

def check_photo_str(path) :
    idx, per = check_photo(path)

    print("이 사진은", labels[idx],"로(으로) 칼로리는 ", calories[idx], "kcal 입니다.")
    print("가능성은 ", per, "% 입니다.")

check_photo_str('test-sushi.jpg')
check_photo_str('test-salad.jpg')
check_photo_str('test-mafa.jpg')