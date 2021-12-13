import urllib.request as req

# 임의 사이트에서
url = "https://images.unsplash.com/photo-1591154669695-5f2a8d20c089?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
# 이미지를 읽어들여 "test.png"로 저장한다.
req.urlretrieve(url,"test.png")

#"opencv"를 이용하여 test.png를 test.jpg로 저장한다.
import cv2
img = cv2.imread("test.png")
cv2.imwrite("test.jpg",img)
#읽어들인 img 형태를 확인해야 한다.
print(img)

#이미지를 화면에 출력한다.
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()