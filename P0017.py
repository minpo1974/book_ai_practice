import pandas as pd

iris_data = pd.read_csv('d:/test/iris.csv', encoding='EUC-KR')

#데이터를 Row형식으로 분리하는 방법을 알 수 있다.
y = iris_data.loc[:, "variety"]
x = iris_data.loc[:, ["sepal.length","sepal.width","petal.length","petal.width"]]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

import warnings
warnings.filterwarnings('ignore')

from sklearn.utils import all_estimators
allAlgorithms = all_estimators(type_filter='classifier')

# K-분할 크로스 밸리데이터 전용 객체
# n_splits - 데이터 분할수
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

kfold_cv = KFold(n_splits=5, shuffle=True)

for(name, algorithm) in allAlgorithms :
    try : 
        # 아래 algorithm 은 인자가 필요함
        if name in ('ClassifierChain', 'MultiOutputClassifier','OneVsOneClassifier','OneVsRestClassifier','OutputCodeClassifier','VotingClassifier'):
            continue
        clf = algorithm()
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        # score메서드를 가진 클래스를 대상으로 하기
        # cross_val_score 함수를 사용할 수 있는 알고리즘을 대상으로 한다.
        if hasattr(clf, 'score'):     # 크로스 밸리데이션
            scores = cross_val_score(clf, x_test, y_test, cv=kfold_cv)
            print(name, "의 정답률=", scores)
            print(name, "의 평균 scores", scores.mean())
    except Exception as e :
        print('지원하지 않는 알고리즘 : ', name)
        #print(e)
        #print('')
