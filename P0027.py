#http://archive.ics.uci.edu/ml/datasets/optical+recognition+of+handwritten+digits

import joblib #pip install joblib
import cv2

def predict_digit(filename) :
    clf = joblib.load("digits.pkl")
    my_img = cv2.imread(filename)
    my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
    my_img = cv2.resize(my_img, (8,8))
    my_img = 15 - my_img #흑백반전
    my_img = my_img.reshape((-1,64))
    res = clf.predict(my_img)
    return res[0]

n = predict_digit("1.png")
print("1.png = " + str(n))

n = predict_digit("2.png")
print("2.png = " + str(n))

n = predict_digit("3.png")
print("3.png = " + str(n))

n = predict_digit("4.png")
print("4.png = " + str(n))

n = predict_digit("5.png")
print("5.png = " + str(n))