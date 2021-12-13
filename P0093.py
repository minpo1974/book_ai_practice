caltech_dir = "./caltechimage/101_ObjectCategories"
categories = ["chair","camera","butterfly","elephant", "flamingo"]
nb_classes = len(categories)

image_w = 64
image_h = 64
pixels = image_w * image_h * 3

x=[]
y=[]

import glob
from PIL import Image
import numpy as np

for idx, cat in enumerate(categories) :
    #print(idx)
    #print(cat)
    label = [0 for i in range(nb_classes)]
    #print(label)
    label[idx] = 1
    #print(label)
    image_dir = caltech_dir + "/" + cat
    #print(image_dir)
    files = glob.glob(image_dir + "/*.jpg")
    #print(files)
    for i , f in enumerate(files) :
        #print(i)
        #print(f)
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        #print(data)
        x.append(data)
        y.append(label)
        #if i% 100 == 0 :
        #    print(i,"\n",data)

import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

x = np.array(x)
y = np.array(y)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y)
xy = (x_train, x_test, y_train, y_test)
np.save("./5obj_1.npy",xy)

print("ok....", len(y))