dbpath = "hw.sqlite3"
select_sql = "select * from person order by id desc limit 20100"

x=[]
y=[]

import sqlite3
import keras
import numpy as np

with sqlite3.connect(dbpath) as conn :
    for row in conn.execute(select_sql) :
        id, height, weight, type_no = row
        height = height / 200
        weight = weight / 150
        y.append(type_no)
        x.append(np.array([height,weight]))

from keras.models import load_model
model = load_model('hw_model.h5')

import os
if os.path.exists('hw_weights.h5') :
    model.load_weights('hw_weights.h5')

import tensorflow as tf
nb_classes = 6
y = tf.keras.utils.to_categorical(y, nb_classes)

model.fit(np.array(x), y, batch_size=50, epochs=100)

model.save_weights('hw_weights.h5')
print('saved')