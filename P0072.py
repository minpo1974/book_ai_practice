from keras.models import load_model

model = load_model('hw_model.h5')
model.load_weights('hw_weights.h5')

x=[]
y=[]

import random
import numpy as np

for i in range(1000) :
    h = random.randint(130, 180)
    w = random.randint(30, 100)
    bmi = w / ((h/100)**2)
    type_no = 1
    if bmi < 18.5 :
        type_no = 0
    elif bmi < 25 :
        type_no = 1
    elif bmi < 30 :
        type_no = 2
    elif bmi < 35 :
        type_no = 3
    elif bmi < 40 :
        type_no = 4
    else :
        type_no = 5
    x.append(np.array([h/200,w/150]))
    y.append(type_no)
    
import tensorflow as tf

x = np.array(x)
y = tf.keras.utils.to_categorical(y, 6)

score = model.evaluate(x, y, verbose=1)
print("정답률=", score[1], "손실률=", score[0])