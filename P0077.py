from typing import no_type_check
import cv2
import numpy as np
import matplotlib.pyplot as plt

photos = np.load('image1/photos1.npz')
x = photos['x']
img = x[12]

plt.figure(figsize=(10,10))

for i in range(36) :
    plt.subplot(6,6,i+1)
    center = (16,16)
    angle = i*5
    scale = 1.0
    mtx = cv2.getRotationMatrix2D(center, angle, scale)
    img2 = cv2.warpAffine(img, mtx,(32,32))

    plt.imshow(img2)

plt.show()
