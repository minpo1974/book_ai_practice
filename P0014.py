import pandas as pd
from sklearn.linear_model import LinearRegression
import piskle

df = pd.read_csv("temp.csv", encoding="EUC-KR")

train_year = (df["일시년"]<=2019)
test_year = (df["일시년"]>=2020)
interval = 6

def make_data(data) :
    x = [] #학습데이터
    y = [] #결과
    temps = list(data["평균기온(°C)"])
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

train_x, train_y = make_data(df[train_year])    
test_x, test_y = make_data(df[test_year])

lr = LinearRegression(normalize=True)
lr.fit(train_x, train_y)

piskle.dump(lr, 'model.pskl')
