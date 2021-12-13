import codecs
from konlpy.tag import Okt


readFp = codecs.open("wikiko.txt", "r", encoding="ISO-8859-1")
gubun_file = "wikiko_iso8859_1.gubun"
writeFp = open(gubun_file, "w", encoding="utf-8")

okt = Okt()
i = 0

while True :
    line = readFp.readline()
    if not line : break
    #print(line)
    if i% 20000 == 0 :
        print("current - " + str(i))
    i += 1
    malist = okt.pos(line, norm=True, stem=True)
    #print(malist)
    r = []
    for word in malist :
        #print("word : ", word)
        #print("word[0] : ", word[0])
        #print("word[1] : ", word[1])
        if not word[1] in ["josa", "Eomi", "Punctuation"] :
            writeFp.write(word[0]+" ")
writeFp.close()
