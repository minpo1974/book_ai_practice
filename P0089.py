import pandas as pd

mr = pd.read_csv("mushroom1.csv", header=None)

label = []
attr_list = []
data = []

for row_index, row in mr.iterrows() :
    #print(row)
    label.append(row[0])
    exdata = []
    for col, v in enumerate(row[1:]) :
        #print("col : ", col)
        #print("v : ", v)
        if row_index == 0 :
            attr = {"dict":{}, "cnt":0}
            attr_list.append(attr)
            #print("attr_list", attr_list)
        else :
            attr = attr_list[col]
            #print("attr :", attr)
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dict"] :
            idx = attr["dict"][v]
        else :
            idx = attr["cnt"]
            attr["dict"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)

    #if row_index == 3 : break

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