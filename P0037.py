import cv2
import os
import glob
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

image_size = (64, 32)
path = os.path.dirname(os.path.abspath(__file__))
#print(path)
path_fish = path + '/fish'
#print(path_fish)
path_nofish = path + '/nofish'
#print(path_nofish)

x = [] #이미지데이터
y = [] #레이블데이터

#이미지 데이터를 배열에 넣기
def read_dir(path, label) :
    files = glob.glob(path + "/*.jpg")
    #print(files)
    for f in files :
        img = cv2.imread(f)
        #cv2.imshow("img", img)
        #cv2.waitKey()
        img = cv2.resize(img, image_size)
        img_data = img.reshape(-1,)
        x.append(img_data)
        y.append(label)

read_dir(path_nofish, 0)
read_dir(path_fish, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
clf = RandomForestClassifier()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

joblib.dump(clf, 'fish.pkl')

#cv2.destroyAllWindows()