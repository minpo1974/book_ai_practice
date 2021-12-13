from sklearn import datasets, svm
# pip install joblib
import joblib
iris=datasets.load_iris()
clf = svm.SVC()
clf.fit(iris.data, iris.target)
joblib.dump(clf,'iris.pkl', compress=True)
