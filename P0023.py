#http://archive.ics.uci.edu/ml/datasets/optical+recognition+of+handwritten+digits

from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

# digits.images => 이미지 데이터
# digits.target => 레이블 데이터
# 8x8, 2차원데이터

for i in range(15) :
    plt.subplot(3,5,i+1)
    plt.axis("off")
    plt.title(str(digits.target[i]))
    plt.imshow(digits.images[i], cmap="gray")

plt.show()

print(digits.images[0])
