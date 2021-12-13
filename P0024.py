#http://archive.ics.uci.edu/ml/datasets/optical+recognition+of+handwritten+digits

from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
import joblib #pip install joblib

digits = datasets.load_digits()

# 이미지 데이터 배열
x = digits.images
# 레이블 데이터
y = digits.target
print("x차원 : ", x.shape)
print("y차원 : ", y.shape)
# 1차원 배열로 변환
x = x.reshape((-1,64))
print(x.shape)
print("x차원 : ", x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

warnings.filterwarnings('ignore')

#
#clf = svm.LinearSVC(C=1.0, class_weight=None, dual=True, 
##                    fit_intercept=True, intercept_scaling=1, 
##                    loss='squared_hinge', max_iter=3000, 
##                    multi_class='ovr', penalty='l2', 
##                    random_state=0, tol=0.0001, verbose=0)
##
clf = svm.LinearSVC()

clf.fit(x_train, y_train)


y_pred = clf.predict(x_test)

print(accuracy_score(y_test, y_pred))

#다중 선형 회귀의 기울기와 절편 결과값
#기울기
w = clf.coef_
#절편
b = clf.intercept_

print('w :',w,'\n b:',b)

#모델 저장하기
#pip install joblib
joblib.dump(clf, 'digits.pkl')
