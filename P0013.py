import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("temp.csv", encoding="EUC-KR")

#2019년까지는 training data
train_year = (df["일시년"]<=2019)
#2020년부터는 testing data
test_year = (df["일시년"]>=2020)
interval = 6 #6일치 data를 의미한다.
#즉, [이전날온도1,이전날온도2,이전날온도3,이전날온도4,이전날온도5,이전날온도6] data 
# ===> [다음날] 결과값
def make_data(data) :
    x = [] #학습데이터
    y = [] #결과
    temps = list(data["평균기온(°C)"]) #평일의 평균기온
    #print(temps)
    for i in range(len(temps)) :
        if i<interval :
            continue
        y.append(temps[i])
        xa = []
        for p in range(interval) :
            d = i + p - interval
            xa.append(temps[d])
        x.append(xa)
    return (x,y)

# train_x 값 형태 : 
# [[4.4, 4.1, 6.5, 7.5, 2.5, 2.8], [4.1, 6.5, 7.5, 2.5, 2.8, -1.1],.....]
train_x, train_y = make_data(df[train_year])    
#print(train_x)
#print(train_y)
test_x, test_y = make_data(df[test_year])

lr = LinearRegression(normalize=True)
lr.fit(train_x, train_y)

pre_y = lr.predict(test_x)

plt.figure(figsize=(10,6), dpi=100)
plt.plot(test_y, c='r')
plt.plot(pre_y, c='b')
plt.savefig('weather-term-lr.png')
plt.show()

#예측과 현실의 차이를 보여준다.
diff_y = abs(pre_y - test_y)

print("차이평균=",sum(diff_y)/len(diff_y))
print("최대차이값=",max(diff_y))
