from konlpy.tag import Okt
from konlpy.tag import Kkma

# JPype1의 버전 문제가 발생시, 
# pip install -U "jpype1<1.1"
# tweepy 패키지 오류가 발생할 경우,
#import tweepy
#print(tweepy.__version__)
#현재의 tweepy 패키지 버전을 낮추어 실행하면 잘 된다.
#version 맞추는 작업을 해야 한다.
#pip install tweepy==3.10.0

okt = Okt()

malist = okt.pos("아버지가방에들어가신다", norm=True, stem=True)
print(malist)

k = Kkma()
malist = k.pos("아버지가방에들어가신다")
print(malist)