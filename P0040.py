import numpy as np
import glob
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def count_codePoint(str) :
    counter = np.zeros(65535)
    for i in range(len(str)) :
        code_point = ord(str[i])
        #print(code_point)
        if code_point > 65535 :
            continue
        counter[code_point] += 1
    counter = counter/len(str)
    return counter

x_train = []
y_train = []

for file in glob.glob('./train/*.txt') :
    print(file[8:10], file)
    y_train.append(file[8:10])
    file_str = ''
    for line in open(file, 'rt', encoding='UTF8') :
        file_str = file_str + line
    x_train.append(count_codePoint(file_str))

clf = GaussianNB()
clf.fit(x_train, y_train)

x_test = []
y_test = []

for file in glob.glob('./test/*.txt') :
    #print(file[7:9], file)
    y_test.append(file[7:9])
    file_str = ''
    for line in open(file, 'rt', encoding='UTF8') :
        file_str = file_str + line
    x_test.append(count_codePoint(file_str))


y_pred = clf.predict(x_test)
print(y_pred)
print("정답률=", accuracy_score(y_test, y_pred))