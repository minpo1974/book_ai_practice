import urllib.request as req

local = "mushroom1.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"

req.urlretrieve(url, local)

print("saved ok")