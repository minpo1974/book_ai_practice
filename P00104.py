import cv2

'''
임계값이 이미지 전체에 적용
영역별로 threshing holding
cv2.adaptiveThreshhold()
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
src – grayscale image
maxValue – 임계값
adaptiveMethod – thresholding value를 결정하는 계산 방법
thresholdType – threshold type
blockSize – thresholding을 적용할 영역 사이즈
C – 평균이나 가중평균에서 차감할 값
Adaptive Method는 아래와 같습니다.
cv2.ADAPTIVE_THRESH_MEAN_C : 주변영역의 평균값으로 결정
cv2.ADAPTIVE_THRESH_GAUSSIAN_C :
'''
img = cv2.imread('dave.jpg',0)

ret, th1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)
titles = ['Original','Global','Mean','Gaussian']
images = [img,th1,th2,th3]

from matplotlib import pyplot as plt

for i in range(4):
	plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])

plt.show()
