'''
- average hash : image를 hash 값으로 변환
MD5, SHA256 ==> 해쉬값을 기반으로 같은 데이터를 검출, 완전동일

1) image => 8x8 ==> 64bit 해쉬값
2) gray scale
3) 각 pixel의 average(평균) 계산
4) pixel의 어두운 정도 평균보다 크면 1, 작으면 0으로...



'''
from PIL import Image
import numpy as np

'''
ANTIALIAS : 위신호제거
'''
def average_hash(fname, size=16) :
    img = Image.open(fname)
    img = img.convert('L') #gray scale
    img = img.resize((size,size), Image.ANTIALIAS)
    pixel_data = img.getdata()
    pixels = np.array(pixel_data)
    #print(pixels)
    pixels = pixels.reshape((size,size))
    #print(pixels)
    avg = pixels.mean()
    #print(avg)
    diff = 1 * (pixels > avg)
    #print(diff)
    return diff

def np2hash(ahash) :
    #print(ahash.tolist())
    bhash=[]
    for nl in ahash.tolist() :
        #print(nl)
        s1 = [str(i) for i in nl]
        #print(s1)
        '''
           '구분자'.join(list)
            => ''.join(list) 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾼다.
            => 리스트 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐준다.
        '''
        s2 = "".join(s1)
        #print(s2)
        i = int(s2,2)
        #print(i)
        '''
         'b0%04x%02x' % (0, 0x0a)
         %04x : 4의 길이를 가진 hexadecimal  => 12 -> 000c
         b0                     -> b0          -> format specifier (X)
         %04x                   ->   0000      -> hexadecimal 4-digit, first value
         %02x                   ->       0a    -> hexadecimal 2-digit, second value
        '''
        bhash.append("%04x" % i)
        #print(bhash)
    return "".join(bhash)

ahash = average_hash("minpopic.jpg")
print(ahash)
print(np2hash(ahash))
