import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import all_estimators
import warnings

#붓꽃 데이터를 읽어들인다.
iris_data = pd.read_csv('d:/test/iris.csv', encoding='EUC-KR')

#붓꽃 데이터를 레이블과 입력 데이터로 분리
y = iris_data.loc[:, "variety"]
x = iris_data.loc[:, ["sepal.length","sepal.width","petal.length","petal.width"]]

#학습전용과 테스트 전용 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

warnings.filterwarnings('ignore')
'''
사이킷런에서는 분류 알고리즘을 구현한 클래스를 Classifier로,
회귀 알고리즘을 구현한 클래스를 Regressor로 지칭하고,
이 둘을 합쳐 Estimator 클래스라고 부른다.
Estimator 클래스는 fit()과 predcict()만을 이용해 간단하게 학습과 예측 결과를 반환한다.

Classifier(분류) : 구현 클래스는 아래와 같다.
 - DecistionTreeClassifier
 - RandomForestClassifier
 - GradientBoostingClassifer
 - GaussianNB
 - SVC
Regressor(회귀) : 구현 클래스는 아래와 같다.
 - LinearRegression
 - Ridge, Lasso
 - RandomForestRegressor
 - GradientBoostingRegressor

 type_filter의 종류
 - classifier
 - regressor
 - cluster
 - transformer
'''
#allAlgorithms = all_estimators(type_filter='classifier')
allAlgorithms = all_estimators()

max_accuracy = 0.0
algorithm_dict = {} #dictionary, name:accuracy 저장

for(name, algorithm) in allAlgorithms :
    try : 
        clf = algorithm()

        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        accuracy_algorithm = accuracy_score(y_test, y_pred)
        algorithm_dict[name] = accuracy_algorithm #알고리즘이름 : accuracy 저장
        if max_accuracy < accuracy_algorithm : #최고 값의 accuracy 저장
            max_accuracy = accuracy_algorithm
        print(name, "의 정답률=", accuracy_algorithm)
    except Exception as e :
        #print('Unable to import', name)
        #print(e)
        #print('')
        #지원하지 않는 알고리즘의 이름을 append한다.
        #print('지원하지 않는 Algorithm: ', name)
        algorithm_dict[name] = -1.0 #알고리즘이름 : accuracy 저장, 오류라는 뜻으로 -1.0 입력

print('전체 알고리즘의 개수는?', len(algorithm_dict.keys()) )

count = 0
for key, value in algorithm_dict.items() :
    if value == -1.0 :
        print(key, ':',value)
        count = count + 1
print('지원하지 않는 알고리즘의 개수는?', len(algorithm_dict.keys())-count)

count = 0
for key, value in algorithm_dict.items() :
    if value != -1.0 :
        print(key, ':',value)
        count = count + 1
print('지원하는 알고리즘의 개수는?', len(algorithm_dict.keys())-count)

print('최고의 accuracy는?', max_accuracy)
for key, value in algorithm_dict.items() :
    if value == max_accuracy :
        print(key, ':',value)
