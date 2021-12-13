import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower_daegoo.jpg")
#원본 이미지를 적절한 크기로 줄인다.
img = cv2.resize(img, (300,169))
#gray로 변경한다.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#이미지에 존재하는 잡음을 제거한다.
gray = cv2.GaussianBlur(gray, (7,7), 0)
#기준을 정하여, 이진화 한다.
#140을 기준으로 0과 1을 만든다. 이 기준은 변경가능하다.
#cv2.threshold(src,thresh,maxval,type,[,dst])->retval,dst
#src : threshold에 적용할 이미지. 다중채널 이미지 또는 Grayscale
#thresh : 임계치
#maxval : thresh를 넘었을 때 적용되는 최대값, 혹은 thresh보다 작을 때 적용되는 최대값
#type : THRESH_BINARY : 픽셀값이 thresh값보다 크면 maxval, 아니면 0
#type : THRESH_BINARY_INV : 픽셀값이 thresh값보다 크면 0, 아니면 maxval
#type : THRESH_TRUNC : 픽셀값이 thresh값보다 크면 thresh적용, 아니면 픽셀값 그대로
#type : THRESH_TOZERO : 픽셀값이 thresh값보다 크면 픽셀값 적용, 아니면 0
#type : THRESH_TOZERO_INV : 픽셀값이 thresh값보다 크면 0, 아니면, 픽셀값 적용


ret, img2 = cv2.threshold(gray, 140, 240, cv2.THRESH_BINARY)
ret, img3 = cv2.threshold(gray, 140, 240, cv2.THRESH_BINARY_INV)
ret, img4 = cv2.threshold(gray, 140, 240, cv2.THRESH_TRUNC)
ret, img5 = cv2.threshold(gray, 140, 240, cv2.THRESH_TOZERO)
ret, img6 = cv2.threshold(gray, 140, 240, cv2.THRESH_TOZERO_INV)

titles = ['original','binary','binary_inv','trunc','tozero','tozero_inv']
images = [gray,img2,img3,img4,img5,img6]

plt.figure(figsize=(8,8))
for i in range(0,6) :
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
