import json
from re import L
import pandas as pd
import matplotlib.pyplot as plt

with open("./lang/freq.json", "r", encoding="utf-8") as fp :
    freq = json.load(fp)

#print(freq[0]["labels"])

lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]) :
    #print(i, lbl)
    fq = freq[0]["freqs"][i]
    #print(fq)
    if not (lbl in lang_dic) :
        lang_dic[lbl] = fq
        #print(lbl)
        #print(lang_dic[lbl])
        continue
    for idx, v in enumerate(fq) :
        #print(idx, v)
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) /2

asclist = [[chr(n) for n in range(97,97+26)]]
df = pd.DataFrame(lang_dic, index=asclist)

plt.style.use('ggplot')
#df.plot(kind="bar", subplots=True, ylim=(0,0.15))
df.plot(kind="line")
plt.savefig("lang-plot.png")
plt.show()