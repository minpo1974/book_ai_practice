from gensim.models import word2vec
from konlpy.tag import Okt

model = word2vec.Word2Vec.load("wikiko.model")
okt = Okt()

def print_emergency(text) :
    print(text)
    node = okt.pos(text, norm=True, stem=True)
    for word, form in node :
        if form =='Noun' or form == 'Verb' or form == 'Adjective' or form == 'Adverb' :
            print("-", word, ":", model.wv.similarity(word, '급하다'))

print_emergency("컴퓨터에 문제가 생겼어요. 빨리 해결해야 하는 문제가 있어서 지원 요청합니다.")
print_emergency("사용 방법을 잘 모르겠어요")
    