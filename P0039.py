import numpy as np
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

ko_str = "안녕하세요. 영산대학교입니다."
ja_str = "こんにちは。霊山大学です。"
en_str = "Hello. Youngsan University."

x_train = [count_codePoint(ko_str), count_codePoint(ja_str), count_codePoint(en_str)]
y_train = ['ko', 'ja','en']

clf = GaussianNB()
clf.fit(x_train, y_train)

ko_test = "저는 영산대 컴공입니다."
ja_test = "私ヨウンサンデコムゴンです。"
en_test = "I am a computer scientist at Yeongsan University."

x_test = [count_codePoint(ko_test), count_codePoint(ja_test), count_codePoint(en_test)]
y_test = ['ko','ja','en']

y_pred = clf.predict(x_test)
print(y_pred)
print("정답률=", accuracy_score(y_test, y_pred))