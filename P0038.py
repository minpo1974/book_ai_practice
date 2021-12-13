from typing import Tuple
import cv2
import joblib
import os
import copy

clf = joblib.load("fish.pkl")
output_dir = "./bestshot"
if not os.path.isdir(output_dir) : os.mkdir(output_dir)

img_last = None
fish_th = 3
count = 0
frame_count = 0

cap = cv2.VideoCapture("fish.mp4")
while True :
    is_ok, frame = cap.read()
    if not is_ok : break
    frame = cv2.resize(frame, (640, 360))
    frame2 = copy.copy(frame)
    frame_count += 1

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15,15),0)
    ret, img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    if not img_last is None :
        frame_diff = cv2.absdiff(img_last, img_b)
        cnts, hierarchy = cv2.findContours(frame_diff,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
        fish_count = 0
        for pt in cnts :
            x,y,w,h = cv2.boundingRect(pt)
            if w <100 or w > 500 : continue
            imgex = frame[y:y+h, x:x+w]
            imagex = cv2.resize(imgex, (64,32))
            image_data = imagex.reshape(-1,)
            pred_y = clf.predict([image_data])
            if pred_y[0] == 1 :
                fish_count += 1
                cv2.rectangle(frame2, (x,y), (x+w, y+h),(0,255,0),2)
        if fish_count > fish_th :
            fname = output_dir + "/fish" + str(count) + ".jpg"
            cv2.imwrite(fname, frame)
            count += 1
    cv2.imshow('FISH!', frame2)
    if cv2.waitKey(1) == 13 : break
    img_last = img_b

cap.release()
cv2.destroyAllWindows()
print("ok", count, "/", frame_count)
