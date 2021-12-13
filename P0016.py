import pandas as pd

iris_data = pd.read_csv('d:/test/iris.csv', encoding='EUC-KR')

y = iris_data.loc[:, "variety"]
x = iris_data.loc[:, ["sepal.length","sepal.width","petal.length","petal.width"]]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

import warnings
warnings.filterwarnings('ignore')

from sklearn.utils import all_estimators
allAlgorithms = all_estimators(type_filter='classifier')

from sklearn.metrics import accuracy_score
for(name, algorithm) in allAlgorithms :
    try : 
        clf = algorithm()
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        print(name, "의 정답률=", accuracy_score(y_test, y_pred))
    except Exception as e :
        print('사용할 수 없는 알고리즘 : ', name)
        #print(e)
        