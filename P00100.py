from PIL import Image
import glob
import numpy as np
import random, math

import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

#root_dir = "./image"
root_dir = "D:/test/httpd-2.4.48-win64-VS16/Apache24/htdocs/image"

categories = ["normal","beni","negi","cheese"]
nb_classes = len(categories)
image_size = 50

X = [] # 이미지 데이터
Y = [] # 레이블 데이터

allfiles = []
for idx, cat in enumerate(categories):
    image_dir = root_dir + "/" + cat
    #print(image_dir)
    files = glob.glob(image_dir + "/*.jpg")
    for f in files:
        allfiles.append((idx, f))

random.shuffle(allfiles)
th = math.floor(len(allfiles) * 0.6)
#print(th)
train = allfiles[0:th]
test  = allfiles[th:]


def make_sample(files, is_train):
    global X, Y
    X = []; Y = []
    for cat, fname in files:
        add_sample(cat, fname, is_train)
    return np.array(X), np.array(Y)

def add_sample(cat, fname, is_train):
    img = Image.open(fname)
    img = img.convert("RGB") # 색상 모드 변경하기
    img = img.resize((image_size, image_size)) # 이미지 크기 변경하기
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)
    if not is_train: return
    for ang in range(-20, 20, 5):
        img2 = img.rotate(ang)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)
        # img2.save("gyudon-"+str(ang)+".PNG")
        # 반전하기
        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)

X_train, y_train = make_sample(train, True)
X_test, y_test = make_sample(test, False)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/gyudon3.npy", xy)
print("학습할 이미지 갯수는? ", len(y_train))