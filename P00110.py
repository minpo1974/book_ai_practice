image_size = 28

import platform
import glob

from numpy.lib.type_check import imag

if platform.system() == "Darwin" :
    ttf_list = glob.glob("/Library/Fonts/*.ttf")
    ttf_list += glob.glob("~/Library/Fonts/*.ttf")
elif platform.system() == "Linux" :
    ttf_list = glob.glob("/usr/share/fonts/*.ttf")
    ttf_list += glob.glob("~/.fonts/*.ttf")
else :
    ttf_list = glob.glob(r"C:\Windows\Fonts\*.ttf")

print("font count=", len(ttf_list))

import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import numpy as np
import cv2
import random

def gen_image(base_im, no, font_name) :
    for ang in range(-20,20,2) :
        sub_im = base_im.rotate(ang)
        data = np.asarray(sub_im)
        X.append(data)
        Y.append(no)
        w = image_size
        for r in range(8,15,3) :
            size = round((r/10) * image_size)
            im2 = cv2.resize(data,(size,size), cv2.INTER_AREA)            
            data2 = np.asarray(im2)
            if image_size > size :
                x = (image_size-size)//2
                data = np.zeros((image_size,image_size))
                data[x:x+size, x:x+size] = data2
            else :
                x = (size-image_size)//2
                data = data2[x:x+w, x:x+w]
            X.append(data)
            Y.append(no)
            if random.randint(0,400) == 0 :
                fname = "image/num/n-{0}-{1}-{2}.png".format(font_name, no, ang, r)
                cv2.imwrite(fname, data)

def draw_text(im, font, text) :
    dr = ImageDraw.Draw(im)
    im_sz = np.array(im.size)
    #print(im.size)
    fo_sz = np.array(font.getsize(text))
    #print(fo_sz)
    xy = (im_sz-fo_sz) / 2
    #print(im_sz, fo_sz, xy)
    dr.text(xy, text, font=font, fill=(255))

    
# 이미지 렌더링하기
X = []
Y = []

for path in ttf_list :
    font_name = os.path.basename(path)
    #print(font_name)
    '''
    트루타입폰트 : 글자의 외곽선만을 저장한 폰트타입
    폰트의 종류, 폰트크기
    '''
    try :
        fo = ImageFont.truetype(path, size=100)
    except :
        continue
    for no in range(10) : #0부터 9까지
        #print(no)
        '''
            1 : 1-bit pixel, black and white, stored with one pixel per byte
            L : 8-bit pixels, black and white
            P : 8-bit pixels, mapped to any other mode using a color palette
            RGB : 3 x 8-bit pixels, true color
            CMYK : 4 x 8-bit pixels, color sparation
            YCbCr : 3 x 8-bit pixels, color video format
            HSV : 3 x 8-bit pixels, Hue, Saturation, Value color space
        '''
        im = Image.new("L", (200,200))
        draw_text(im, fo, str(no))
        #im.save("pixel_test.jpg")
        ima = np.asarray(im)
        blur = cv2.GaussianBlur(ima, (5, 5), 0)  # 블러
        th = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)  # 2진 변환
        contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
        for cnt in contours :
            x,y,w,h = cv2.boundingRect(cnt)
            if w < 10 or h < 10 :
                continue
        num = ima[y:y+h, x:x+w]
        ww = w if w > h else h
        wx = (ww - w) // 2
        wy = (ww - h) // 2
        spc = np.zeros((ww, ww))
        spc[wy:wy+h, wx:wx+w] = num
        num = cv2.resize(spc, (image_size, image_size), cv2.INTER_AREA)
        X.append(num)
        Y.append(no)
        base_im = Image.fromarray(np.uint8(num))
        gen_image(base_im, no, font_name)

if not os.path.exists("./image/num") :
    os.makedirs("./image/num")

X = np.array(X)
Y = np.array(Y)
np.savez("./image/font_draw1.npz", x=X, y=Y)
print("ok, 다양한 각도의 숫자 이미지가 ", len(Y), "개 생성되었습니다.")