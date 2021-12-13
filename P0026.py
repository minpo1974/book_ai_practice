#http://archive.ics.uci.edu/ml/datasets/optical+recognition+of+handwritten+digits

from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
import joblib #pip install joblib

digits = datasets.load_digits()

x = digits.images
y = digits.target

x = x.reshape((-1,64))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

warnings.filterwarnings('ignore')

#
#clf = svm.LinearSVC(C=1.0, class_weight=None, dual=True, 
##                    fit_intercept=True, intercept_scaling=1, 
##                    loss='squared_hinge', max_iter=3000, 
##                    multi_class='ovr', penalty='l2', 
##                    random_state=0, tol=0.0001, verbose=0)
##

clf = joblib.load("digits.pkl")

y_pred = clf.predict(x_test)

print(accuracy_score(y_test, y_pred))
