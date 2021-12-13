#wine 품질 판정 만들기
import pandas as pd

wine = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8" )

#quality 기준으로 대상 데이터 수 표현
wine_g = wine.groupby(['quality'])["quality"].count()
print(wine_g)
wine_g.plot()

import matplotlib.pyplot as plt
#plot의 결과를 파일에 저장한다.
plt.savefig("wine-count-plt.png")
#plot을 화면에 보여준다.
plt.show()


