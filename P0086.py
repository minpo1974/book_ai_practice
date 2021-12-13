import pandas as pd

tbl = pd.read_csv("bmi_test.csv", index_col=2)
#print(tbl)

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1) # 1행1열, 세번째 인자 1은 첫번째 subplot

def scatter(lbl, color) :
    b = tbl.loc[lbl]
    #print(b)
    ax.scatter(b["weight"],b["height"], c=color, label=lbl)

scatter("fat", "red")
scatter("normal","yellow")
scatter("thin","purple")
ax.legend()
plt.show()