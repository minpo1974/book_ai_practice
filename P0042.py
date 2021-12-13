# pip install SudachiPy
# pip install sudachidict_core
# pip install sudachidict_small
# pip install sudachidict_full

import codecs
from sudachipy import tokenizer
from sudachipy import dictionary

readFp = codecs.open("wikija.txt", "r", encoding="utf-8")
gubun_file = "wikija.gubun"
writeFp = open(gubun_file, "w", encoding="utf-8")

i = 0

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.A

while True :
    line = readFp.readline()
    print(line)
    print([m.surface() for m in tokenizer_obj.tokenize(line, mode)])

    if not line : break
    if i == 5 :
        print("current - " + str(i))
        break
    i += 1