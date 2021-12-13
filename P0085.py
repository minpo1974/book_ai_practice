import pandas as pd

tbl = pd.read_csv("bmi_test.csv")

label = tbl["label"]
#print(label)

w = tbl["weight"]/100
h = tbl["height"]/200

wh = pd.concat([w,h], axis = 1) #axis : 같은 키값에 해당하는 데이터를 가로로 넣을 수 있다.
#print(wh)

from sklearn.model_selection import train_test_split
data_train, data_test, label_train, label_test = train_test_split(wh, label)

from sklearn import svm
import time

count_t = time.time()
#clf = svm.SVC() #running time : 0.56549, 정답률: 0.9944
#clf = svm.NuSVC() #running time : 9.41185, 정답률: 0.9488
clf = svm.LinearSVC() #running time : 0.05785, 정답률: 0.9278
clf.fit(data_train, label_train)

print("Running Time : %.05f" % (time.time()-count_t))

predict = clf.predict(data_test)

from sklearn import metrics
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print("정답률 = ", ac_score)
print("리포트=\n", cl_report)