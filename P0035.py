import cv2

cap = cv2.VideoCapture(0)

fmt = cv2.VideoWriter_fourcc('m','p','4','v')
fps = 20.0
size = (640,360)
writer = cv2.VideoWriter('test.m4v', fmt, fps, size)

while True :
    _,frame = cap.read()
    frame = cv2.resize(frame,size)
    writer.write(frame)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 13 : break

writer.release()
cap.release()
cv2.destroyAllWindows()
