'''
임계값을 사용자가 결정하여...
여러분은 어떻게 임계값을 결정해야 하는가?
trial and error

bimodal image
Otsu's Binarization : bimodal image에서 임계값을 자동으로 계산해주는 것을 말한다.
cv2.threshhod() 함수에서 flag를 추가, cv2.THRESH_OTSU, 0으로 전달
'''
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

#img = cv2.imread('dave.jpg',0)
img = cv2.imread('noise.jpg',0)
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img, 0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img,(5,5),0)
ret3, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 
          'Original Noisy Image','Histogram',
        "Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
	plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
	plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
	plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
	plt.title(titles[i*3+2]), plt.xticks([])

plt.show()
