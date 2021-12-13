import cv2
# https://github.com/opencv/opencv/tree/master/data/haarcascades

#다운 받은 파일을 변수에 지정한다.
cascade_file = "haarcascade_frontalface_default.xml"
eye_file = "haarcascade_eye.xml"

#cv2.CascadeClassifier 함수를 통해 읽어들인다.
face_cascade = cv2.CascadeClassifier(cascade_file)
eye_cascade = cv2.CascadeClassifier(eye_file)

#물리적인 카메라와 연결한다.
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#물리적인 카메라에서 영상을 읽어온다.(사람얼굴)
while(True) :
    ret, frame = cap.read()
    #Gray scale로 변환한다.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #검출된 얼굴을 face_list에 저장한다.
    face_list = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("검출된 얼굴의 수 ", len(face_list))
    for (x,y,w,h) in face_list :
        #얼굴의 위치는 (x,y,w,h) 형태의 tuple이다. (x,y)는 검출된 얼굴의 좌상단 위치이고 (w,h)는 검출된 얼굴의 가로와 세로 크기이다.
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        img_gray = cv2.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), 2)
        #gray scale 정보
        roi_gray = img_gray[y:y+h, x:x+w]
        #color scale 정보
        roi_color = img[y:y+h, x:x+w]
        #gray scale에서 눈을 검출한다.
        eyes = eye_cascade.detectMultiScale(roi_gray)
        print("검출된 눈의 수 ", len(eyes))
        for (ex,ey,ew,eh) in eyes :
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    cv2.imshow('gray', gray)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        cv2.imwrite("myface.png",roi_color)
        break

cap.release()
cv2.destroyAllWindows()