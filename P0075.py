import numpy as np

photos = np.load("image1/photos1.npz")

x = photos['x']
y = photos['y']

idx = 200

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
for i in range(25) :
    plt.subplot(5,5,i+1)
    plt.title(y[i+idx])
    plt.imshow(x[i+idx])

plt.show()