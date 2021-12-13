import pandas as pd

mr = pd.read_csv("mushroom1.csv", header=None)
label = []
data = []
for row_index, row in mr.iterrows() :
    #print(row[0])
    label.append(row[0])
    row_data = []
    for v in row[1:] :
        row_data.append(ord(v))
    data.append(row_data)
#print(label)
#print(row_data)
#print(data)

from sklearn.model_selection import train_test_split
data_train, data_test, label_train, label_test = train_test_split(data, label)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

from sklearn import metrics
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print("정답률:", ac_score)
print("리포트=\n", cl_report)