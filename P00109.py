from re import X
import P00108
import cv2

mnist = P00108.build_model()
mnist.load_weights('mnist_1.hdf5')

im = cv2.imread('numbers100.png')

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5),0)
thresh = cv2.adaptiveThreshold(blur, 255,1,1,11,2)
cv2.imwrite('numbers100-th1.png', thresh)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

rects = []
#print(im.shape)
im_w = im.shape[1]
#print(im_w)

im_th = cv2.imread('numbers100-th1.png')

for i, cnt in enumerate(contours) :
    x,y,w,h = cv2.boundingRect(cnt)
    if w<10 or h < 10 : continue
    if w > im_w /5 : continue
    '''
    round() 사사오입 원칙
    반올림할 자리의 수가 5이면 반올림할 때,
    앞자리의 숫자가 짝수면 내림
    앞자리의 숫자가 홀수면 올림
    round(4.5) =-> 4
    round(3.5) #-> 4
    '''
    y2 = round(y/10) *10 # y좌표맞추기
    #print(y2)
    red = (0,0,255)
    cv2.rectangle(im_th,(x,y),(x+w,y+h), red, 2)
    index = y2*im_w + x

    rects.append((index,x,y,w,h))
rects = sorted(rects, key=lambda x:x[0])
#print(rects)
cv2.imwrite('numberscnt_rectangle.png',im_th)

import numpy as np

X=[]
for i, r in enumerate(rects) :
    #print(r)
    index, x, y, w,h = r
    num = gray[y:y+h, x:x+w]
    #print(num[0])
    num = 255-num #반전
    #print(num[0])
    ww = round((w if w > h else h) * 1.85)
    #print(ww)
    spc = np.zeros((ww,ww))
    wy = (ww-h)//2
    wx = (ww-w)//2
    spc[wy:wy+h, wx:wx+w] = num
    num = cv2.resize(spc,(28,28)) #Mnist 크기 맞추기
    #cv2.imwrite(str(i)+"-num1.png",num)
    num = num.reshape(28*28)
    num = num.astype("float32")/255
    X.append(num)

s = "31415926535897932384" + \
    "62643383279502884197" + \
    "16939937510582097494" + \
    "45923078164062862089" + \
    "98628034825342117067"

answer = list(s)
#print(answer)
ok = 0
nlist = mnist.predict(np.array(X))
for i, n in enumerate(nlist) :
    ans = n.argmax()
    if ans == int(answer[i]) :
        ok += 1
    else :
        print("[ng]", i, "번째", ans, "!=", answer[i], np.int32(n*100))
print("정답률:", ok/len(nlist))
    

