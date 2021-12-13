#2. wine data reading

import pandas as pd
df = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8" )
print(df)
