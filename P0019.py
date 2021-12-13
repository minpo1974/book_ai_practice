import cv2
import matplotlib.pyplot as plt

img = cv2.imread("test.jpg")

#배열[y1:y2, x1:x2]
#이미지 영역의 일부를 잘라내는 방법
img2 = img[150:450, 150:450]

plt.axis("off")
#BGR로 읽어온다.
plt.imshow(img2)
plt.show()

#RGB로 읽어온다.
plt.axis("off")
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()