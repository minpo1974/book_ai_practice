from tensorflow.keras.datasets import cifar10

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

import matplotlib.pyplot as plt
from PIL import Image

plt.figure(figsize=(10,10))

labels = ["airplane", "automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

print(y_train[0][0])
print(labels[y_train[0][0]])

for i in range(0,40) :
    im = Image.fromarray(x_train[i])
    plt.subplot(5,8, i+1)
    plt.title(labels[y_train[i][0]])
    plt.tick_params(labelbottom="off", bottom="off")
    plt.tick_params(labelleft="off",left="off")
    plt.imshow(im)
plt.show()
print(x_train)
print(x_train[0])
print(x_train[0].shape)
im = Image.fromarray(x_train[0])
plt.imshow(im)
plt.show()
