import enum
from keras.datasets import mnist
import P00108
import cv2

mnist = P00108.build_model()
mnist.load_weights('font_draw1.hdf5')

im = cv2.imread('numbers100.png')

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blur, 255,1,1,11,2)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

rects = []
im_w = im.shape[1]

for i, cnt in enumerate(contours) :
    x,y,w,h = cv2.boundingRect(cnt)
    if w<10 or h < 10 : continue
    if w > im_w/5 : continue

    y2 = round(y/10) * 10
    index = y2*im_w + x
    rects.append((index,x,y,w,h))

rects = sorted(rects, key=lambda x : x[0])

import numpy as np
X=[]

for i, r in enumerate(rects) :
    index,x,y,w,h = r
    num = gray[y:y+h, x:x+w]
    num = 255-num
    #ww = round((w if w > h else h) * 1.85)
    ww = round((w if w > h else h) * 1.2)
    spc = np.zeros((ww,ww))
    wy = (ww-h)//2
    wx = (ww-w)//2
    spc[wy:wy+h, wx:wx+w] = num
    num = cv2.resize(spc,(28,28))
    num = num.reshape(28*28)
    num = num.astype("float32")/255
    X.append(num)

s = "31415926535897932384" + \
    "62643383279502884197" + \
    "16939937510582097494" + \
    "45923078164062862089" + \
    "98628034825342117067"

answer = list(s)
ok = 0
nlist = mnist.predict(np.array(X))
for i, n in enumerate(nlist) :
    ans = n.argmax()
    if ans == int(answer[i]) :
        ok += 1
    else :
        print("[ng]", i,"번째", ans,"!=",answer[i],np.int32(n*100))
    
print("정답률 : ", ok/len(nlist))

