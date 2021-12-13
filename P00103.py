import cv2

'''
이진화 처리 : 영상을 흑/백으로 분류 처리하는 것을 말한다.
이때 기준이 되는 임계값을 어떻게 결정할 것인가?
임계값보다 크다면, 백, 작으면 흑
기본 : 사용자가 고정된 임계값을 사용

cv2.threshhod(src, thresh, maxval, type) -> retval, dst
src : input image, single-channel image(gracyscale image)
thresh : 임계값
maxval : 이 값을 넘었을 때 적용할 값
type : threshholding type (THRESH_BINARY, BINARY_INV, TRUNC, TOZERO, TOZERO_INV)

'''
im = cv2.imread('gradient.jpg')

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

ret, thresh1 = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(im, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(im, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(im, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'BINARY', 'BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [im, thresh1, thresh2, thresh3,thresh4, thresh5]

from matplotlib import pyplot as plt

for i in range(6) :
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    
plt.show()
