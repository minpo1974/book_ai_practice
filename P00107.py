import cv2

im = cv2.imread('numbers100.png')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5), 0)

thresh = cv2.adaptiveThreshold(blur, 255, 1,1,11,2)
'''
중복 검출
계층구조를 가진 윤곽도 검출
얼굴(눈/코)
findcontours매개 변수를 변경
두번째, cv2.RETR_EXTERNAL : 가장 외곽 부분만 검출
'''

#contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

for cnt in contours :
    x,y,w,h = cv2.boundingRect(cnt)
    if h < 20 : continue
    red = (0,0,255)
    cv2.rectangle(im,(x,y),(x+w,y+h), red, 2)

cv2.imwrite('numberscnt100.png', im)