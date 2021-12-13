import cv2

# https://github.com/opencv/opencv/tree/master/data/haarcascades

def mosaic(img, rect, size) :
    (x1, y1, x2, y2) = rect
    w = x2-x1
    h = y2-y1
    #얼굴로 인식되는 영역을 구한 뒤,
    i_rect = img[y1:y2, x1:x2]
    #resize함수로 size를 확대/축소
    i_small = cv2.resize(i_rect,(size,size))
    i_mos = cv2.resize(i_small,(w,h), interpolation=cv2.INTER_AREA)
    #원본 이미지에 
    img2 = img.copy()
    #모자이크된 이미지를 덮어쓴다.
    img2[y1:y2,x1:x2] = i_mos
    #모자이크된 이미지를 return
    return img2

cascade_file = "haarcascade_frontalface_default.xml"
eye_file = "haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(cascade_file)
eye_cascade = cv2.CascadeClassifier(eye_file)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while(True) :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_list = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(len(face_list))
    for (x,y,w,h) in face_list :
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        img_gray = cv2.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), 2)

        roi_gray = img_gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex, ey,ew,eh) in eyes :
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        #size 15를 변경하면, 모자이크의 세밀도가 달라진다.
        mos = mosaic(img, (x,y,x+w,y+h), 15)
        mos_gray = mosaic(img_gray,(x,y,x+w,y+h), 5)

        cv2.imshow('mos', cv2.cvtColor(mos, cv2.COLOR_BGR2RGB))
        cv2.imshow('mos_gray', cv2.cvtColor(mos_gray, cv2.COLOR_BGR2RGB))

    cv2.imshow('gray', gray)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()