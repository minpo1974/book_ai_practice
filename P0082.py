from sklearn import svm
import json
import joblib

with open("./lang/freq.json", "r", encoding="utf-8") as fp :
    d = json.load(fp)
    data = d[0]
#print(data)
clf = svm.SVC()
clf.fit(data["freqs"],data["labels"])

joblib.dump(clf,"./lang/freq.pkl")
print("saved ok")


