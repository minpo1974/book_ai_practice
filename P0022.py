import cv2
from scipy import ndimage
import matplotlib.pyplot as plt

def face_detect(img) :
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_list = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    for(x,y,w,h) in face_list :
        print("얼굴의 좌표=", x,y,w,h)
        red = (0,0,255)
        cv2.rectangle(img,(x,y),(x+w,y+h), red, thickness=30)

cascade_file = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_file)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while(True) :
    ret, frame = cap.read()

    for i in range(0,9) : #0~8
        # 곱해지는 3 숫자를 변경해가면서 인식되는 정도를 확인
        ang = i * 3
        print("--" + str(ang) + "--")
        #image를 angle 각도로 회전시킨다.
        img_r = ndimage.rotate(frame, ang)
        #회전시킨 이미지를 face_detect 함수에 입력한다.
        face_detect(img_r)
        #3*3 행렬로 9개의 이미지를 배치한다.
        plt.subplot(3,3,i+1) 
        plt.axis("off")
        plt.title("face angle=" + str(ang))
        plt.imshow(cv2.cvtColor(img_r, cv2.COLOR_BGR2RGB))
    
    plt.show()

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()
