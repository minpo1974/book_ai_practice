import cv2
import os

img_last = None
no = 0
save_dir = "./exfish"

if not os.path.isdir(save_dir) : os.mkdir(save_dir)

cap = cv2.VideoCapture("fish.mp4")

while True :
    is_ok, frame = cap.read()
    if not is_ok : break
    frame = cv2.resize(frame, (640,360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15,15), 0)
    ret, img_b = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    if not img_last is None :
        frame_diff = cv2.absdiff(img_last, img_b)
        cnts, hierarchy = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for pt in cnts :
            x,y,w,h = cv2.boundingRect(pt)
            if w < 100 or w > 500 : continue
            imagex = frame[y:y+h, x:x+w]
            outfile = save_dir + "/" + str(no) + ".jpg"
            cv2.imwrite(outfile, imagex)
            no += 1
    img_last = img_b
cap.release()
print("OK")