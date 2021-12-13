import cv2
import numpy as np

cap = cv2.VideoCapture(0)

arr = np.array([
                [
                   [1, 2, 3, 4], [5, 6, 7, 8]
                ], 
                [
                   [1, 2, 3, 4], [5, 6, 7, 8]
                ], 
                [
                   [1, 2, 3, 4], [5, 6, 7, 8]
                ]
               ]
              )
print(arr.shape)
print(arr[:,:,0])

arr[:,:,0] = 0
print(arr[:,:,0])
while True :
    _, frame = cap.read()
    frame = cv2.resize(frame, (500, 300))
    #print(frame)
    frame[:,:,0] = 0 #파란색을 0
    frame[:,:,1] = 0 #초록색을 0

    cv2.imshow('RED Camera', frame)
    k = cv2.waitKey(1000)
    if k == 27 or k == 13 : break

cap.release()
cv2.destroyAllWindows()
