from keras.models import load_model

model = load_model('hw_model.h5')
model.load_weights('hw_weights.h5')

labes = ['저체중','표준체중','1비만(1도)','비만(2도)','비만(3도)','비만(4도)']

height = 160
weight = 50

text_x = [height/200, weight/150]

import numpy as np
pre = model.predict(np.array([text_x]))
print(pre[0])
idx = pre[0].argmax()
print(labes[idx], '/ 가능성 : ', pre[0][idx])