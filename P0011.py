import pandas as pd
df = pd.read_csv("temp.csv", encoding="EUC-KR")

g = df.groupby(['일시월'])['평균기온(°C)']
gg = g.sum() / g.count()

print(gg)
gg.plot()

import matplotlib.pyplot as plt
plt.savefig("temp-month-avg.png")
plt.show()