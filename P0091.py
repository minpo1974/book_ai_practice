'''
http://www.vision.caltech.edu/archive.html
caltech 101 download
'''

from PIL import Image
import numpy as np
import os
import re

from numpy.lib.function_base import diff

#파일 경로
search_dir = "./caltechimage/101_ObjectCategories"
cache_dir = "./caltechimage/cache_avhash1"

if not os.path.exists(cache_dir) :
    os.mkdir(cache_dir)

def average_hash(fname, size=16) :
    fname2 = fname[len(search_dir):]
    #print(fname2)
    cache_file = cache_dir + "/" + fname2.replace('/','_') + ".csv"
    #print(cache_file)
    if not os.path.exists(cache_file) :
        img = Image.open(fname)
        img = img.convert('L').resize((size,size), Image.ANTIALIAS)
        pixels = np.array(img.getdata()).reshape((size,size))
        avg = pixels.mean()
        px = 1 *(pixels > avg)        
        np.savetxt(cache_file, px, fmt="%.0f", delimiter=",")
    else :
        px = np.loadtxt(cache_file, delimiter=",")
    #print(px)
    return px

'''
Hamming distance
곱집합 위에 정의되는 거리 함수
대략, 같은 길이의 두 문자열에서, 같은 위치에서 서로 다른 기호들이 몇개인지 counting
'1011101'
'1001001' ==> 해밍거리는 2
'toned'
'roses'  ==> 해밍거리는 3
'''
def hamming_dist(a, b) :
    aa = a.reshape(1,-1)
    ab = b.reshape(1,-1)
    dist = (aa != ab).sum()
    #print(dist)
    return dist

def enum_all_files(path) :
    '''
    os.walk()
    하위의 폴더들을 for 문으로 탐색
    root : dir과 files가 있는 path
    dirs : root 폴더 아래에 있는 폴더들
    files : root 폴더 아래에 있는 파일들
    '''
    path = path + "/"
    for root, dirs, files in os.walk(path) :
        #print(files)
        for f in files :
            #print(f)
            fname = os.path.join(root, f)
            fname = fname.replace("\\","/")
            #print(fname)
            if re.search(r'\.(jpg|jpeg|png)$',fname) :
                #print(fname)
                yield fname

def find_image(fname, rate) :
    src = average_hash(fname)
    for fname in enum_all_files(search_dir) :
            dst = average_hash(fname)
            diff_r = hamming_dist(src, dst) / 256
            if diff_r < rate :
                yield(diff_r, fname)


srcfile = search_dir + "/chair/image_0016.jpg"
sim = list(find_image(srcfile, 0.25))

sim = sorted(sim, key=lambda x : x[0])

html = ""

for r, f in sim :
    print(r,">", f)
    s = '<div style="float:left;"><h3>[ 차이 : ' + str(r) + '-' + os.path.basename(f) + ']</h3>' + '<p><a href="'+f+'"><img src="'+f+'" width=400>'+'</a></p></div>'
    #print(s)
    html += s
#print(html)
html = """<html><head><meta charset="utf8"></head><body><h3>원래이미지</h3></p><img src='{0}' width=400></p>{1}</body></html>""".format(srcfile, html)
#print(html)
with open("./avhash-search-output1.html","w", encoding="utf-8") as f :
    f.write(html)
f.close()
print("ok")
#print("sim[0]", sim[0])
#print("sim[0][0]", sim[0][0])
#average_hash(srcfile)
#enum_all_files(search_dir)
