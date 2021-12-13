import cv2
import matplotlib.pyplot as plt

def detect_zipno(fname, option) :
    img = cv2.imread(fname)
    h, w = img.shape[:2]
    #print(h, w)
    if option == 0 : #보내는 사람
        img = img[80:150, 50:180]
    else : #받는 사람
        img = img[190:260, 390:600]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3,3), 0)
    ret, img2 = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)

    cnts, hierarchy = cv2.findContours(img2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    result = []
    for pt in cnts :
        x, y, w, h = cv2.boundingRect(pt)
        #print(w)
        if not(2 < w < 80) : continue
        result.append([x,y,w,h])
    #print(result)

    result = sorted(result, key=lambda x:x[0])
    #print(result)

    result2 = []
    lastx = -100
    for x, y, w,h in result :
        #print(x-lastx)
        if (x-lastx) < 10 : continue
        result2.append([x,y,w,h])
        lastx = x

    #print(result2)
    for x,y,w,h in result2 :
        #print(x,y,x+w,y+h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 1)

    return result2, img

cnts1, img1 = detect_zipno("postal_envelop.png", 0) #보내는사람
print(cnts1)
cnts2, img2 = detect_zipno("postal_envelop.png", 1) #받는사람
print(cnts2)
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.savefig("detect-zip.png",dpi=200)

plt.show()
