#이미지를 프로젝트 폴더에 복사해 오거나,
#웹서버의 image 처리 폴더를 지정해준다.

#root_dir = "./image"
root_dir = "D:/test/httpd-2.4.48-win64-VS16/Apache24/htdocs/image"
categories = ["normal","beni","negi","cheese"]
nb_classes = len(categories)
image_size = 50

x = [] #이미지데이터
y = [] #레이블데이터

import glob
from PIL import Image
import numpy as np

for idx, cat in enumerate(categories) :
    image_dir = root_dir + "/" + cat
    #print(image_dir)
    files = glob.glob(image_dir + "/*.jpg")
    #print(files)
    print("---", cat, "처리 중")
    for i, f in enumerate(files) :
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_size, image_size))
        data = np.asarray(img)
        x.append(data)
        y.append(idx)

import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

x = np.array(x)
y = np.array(y)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y)

xy = (x_train, x_test, y_train, y_test)

np.save("./image/gyudon1.npy", xy)
print("ok", len(y))