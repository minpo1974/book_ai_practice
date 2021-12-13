outfile = "image1/photos1.npz"
max_photo = 100
photo_size = 32

x=[] #이미지데이터
y=[] #레이블데이터

import glob
import random
from PIL import Image
import numpy as np

def glob_files(path, label) :
    files = glob.glob(path + "/*.jpg")
    random.shuffle(files)
    num = 0
    for f in files :
        #if num >= max_photo : break
        num +=1
        img = Image.open(f)        
        img = img.convert("RGB")
        img = img.resize((photo_size, photo_size))
        img = np.asarray(img)
        x.append(img)
        y.append(label)

glob_files("./image1/sushi",0)
glob_files("./image1/salad",1)
glob_files("./image1/tofu",2)

np.savez(outfile, x=x, y=y)

print("저장했습니다.")
