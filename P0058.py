import glob, os
import struct
from PIL import Image, ImageEnhance

outdir = "png-etl1/"
if not os.path.exists(outdir) : os.mkdir(outdir)

files = glob.glob("ETL1/*")

for fname in files :
    if fname == outdir+"ETL1/ETL1INFO" :
        continue
    #print(fname)
    f = open(fname,'rb')
    f.seek(0)
    while True :
        #메타데이터와 이미지 데이터 조합을 하나씩 읽어들이기
        s = f.read(2052)
        if not s : break
        #바이너리 데이터, python에서 읽어올수 있는 데이터형태로 변형
        r = struct.unpack('>H2sH6BI4H4B4x2016s4x', s)
        code_ascii = r[1]
        #print(code_ascii)
        code_jis = r[3]
        #print(code_jis)
        #이미지 데이터로 추출
        iF = Image.frombytes('F',(64,63), r[18], 'bit',4)
        iP = iF.convert('L')

        #이미지를 선명하가게해서 저장
        dir = outdir+str(code_jis)
        if not os.path.exists(dir) : os.mkdir(dir)

        fn = "{0:02x}-{1:02x}{2:04x}.png".format(code_jis, r[0], r[2])
        #print(fn) 
        fullpath = dir + "/" + fn
        #print(fullpath)
        enhancer = ImageEnhance.Brightness(iP)
        iE = enhancer.enhance(16)
        iE.save(fullpath, 'PNG')
print("OK")