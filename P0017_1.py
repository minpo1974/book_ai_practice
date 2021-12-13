import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.utils import all_estimators
import warnings

#붓꽃 데이터를 읽어들인다.
iris_data = pd.read_csv('d:/test/iris.csv', encoding='EUC-KR')

#붓꽃 데이터를 레이블과 입력 데이터로 분리한다.
#데이터를 Row형식으로 분리하는 방법을 알 수 있다.
y = iris_data.loc[:, "variety"]
x = iris_data.loc[:, ["sepal.length","sepal.width","petal.length","petal.width"]]

#학습전용과 테스트 전용 분리한다.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

warnings.filterwarnings('ignore')
#allAlgorithms = all_estimators(type_filter='classifier')
allAlgorithms = all_estimators()

max_accuracy = 0.0
algorithm_dict = {} #dictionary, name:accuracy 저장

# n_splits - 데이터 분할수
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# K-분할 크로스 밸리데이터 전용 객체
# n_splits 숫자에 따라 , [0.83333333 0.83333333 1.         0.83333333 1.        ]의 출력 개수가 변경된다.
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
            algorithm_dict[name] = scores.mean() #알고리즘이름 : accuracy 저장
            if max_accuracy < scores.mean() : #최고 값의 accuracy 저장
                max_accuracy = scores.mean()

            print(name, "의 정답률=", scores)
            print(name, "의 평균 scores", scores.mean())
            
    except Exception as e :
        #print('지원하지 않는 알고리즘 : ', name)
        #print(e)
        #print('')
        algorithm_dict[name] = -1.0 #알고리즘이름 : accuracy 저장, 오류라는 뜻으로 -1.0 입력

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
