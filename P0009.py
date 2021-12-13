import pandas as pd

in_file = "OBS_ASOS_DD_20211203133447.csv"
out_file = "temp.csv"

temp = pd.read_csv("OBS_ASOS_DD_20211203133447.csv", sep=",", encoding="EUC-KR")

df = pd.DataFrame(temp, columns=['일시','평균기온(°C)'])
df['일시년'] = df.일시.str.split('-').str[0]
df['일시월'] = df.일시.str.split('-').str[1]
df['일시일'] = df.일시.str.split('-').str[2]

dg = pd.DataFrame(df, columns=['일시년','일시월','일시일','평균기온(°C)'])
print(dg)

dg.to_csv(out_file, header=True, index=False,encoding="EUC-KR")
