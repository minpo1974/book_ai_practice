import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower_daegoo.jpg")
#원본 이미지를 적절한 크기로 줄인다.
img = cv2.resize(img, (300,169))
#gray로 변경한다.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#이미지에 존재하는 잡음을 제거한다.
gray = cv2.GaussianBlur(gray, (7,7), 0)

#contour 추출모드 : 두 번째 인자, return 값인 hierachy 값에 영향을 준다.
#type : cv2.RETR_TREE : 이미지에서 모든 contour를 추출하고, contour들간의 상관관계를 추출
#type : cv2.RETR_EXTERNAL : 이미지의 가장 바깥쪽의 contour만 추출
#type : cv2.RETR_LIST : Contour간의 계층구조 상관관계를 고려하지 않고 contour 추출
#type : cv2.RETR_CCOMP : 이미지에서 모든 contour를 추출 후, 2단계 contour 계출 구조로 구성, 1단계에서는 외곽 경계부분, 2단계에서는 hole의 경계부분을 표현
#CHAIN_ : 세번째 인자, contour 근사 방법
#type : cv2.CHAIN_APPROX_NONE : contour를 구성하는 모든 점을 저장함
#type : cv2.CHAIN_APPROX_SIMPLE : contour의 수평,수직, 대각선 방향의 점은 모두 버리고 끝점만 남겨둠
#type : cv2.CHAIN_APPROX_TC89_1 : Teh-Chin 연결근사 알고리즘을 적용함

ret, img2 = cv2.threshold(gray, 140, 240, cv2.THRESH_BINARY)
ret, img3 = cv2.threshold(gray, 140, 240, cv2.THRESH_BINARY_INV)
ret, img4 = cv2.threshold(gray, 140, 240, cv2.THRESH_TRUNC)
ret, img5 = cv2.threshold(gray, 140, 240, cv2.THRESH_TOZERO)
ret, img6 = cv2.threshold(gray, 140, 240, cv2.THRESH_TOZERO_INV)

titles = ['original','binary','binary_inv','trunc','tozero','tozero_inv']
images = [gray,img2,img3,img4,img5,img6]

plt.figure(figsize=(8,8))
for i in range(0,6) :
    #윤곽선을 검출한다.
    cnts, hierarchy = cv2.findContours(images[i], cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #검출된 윤곽선에 사각형을 그린다.
    for pt in cnts :
        x, y, w, h = cv2.boundingRect(pt)
        if w < 30 or w > 200 : continue
        #print(x,y,w,h)
        cv2.rectangle(images[i],(x,y),(x+w,y+h),(0,255,0),2)
    cv2.drawContours(images[i], cnts, -1, (0,0,255),3)
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

