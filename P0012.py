import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("temp.csv", encoding="EUC-KR")

hot_bool = (df["평균기온(°C)"]>30)

hot = df[hot_bool]

cnt = hot.groupby(["일시년"])["일시년"].count()

print(cnt)
cnt.plot()
plt.savefig("tem-over30.png")
plt.show()
