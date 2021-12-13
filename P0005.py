#1. wine data 받기
from urllib.request import urlretrieve
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/" + "winequality-white.csv"
savepath = "winequality-white.csv"
urlretrieve(url, savepath)
