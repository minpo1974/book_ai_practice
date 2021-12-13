import os.path
import joblib
import html
import cgi

#학습 데이터 읽어오기

pklfile = os.path.dirname(__file__) + "/lang/freq.pkl"
#print(pklfile)
clf = joblib.load(pklfile)

#웹 페이지에서 보여줄 페이지를 만듬
#HTML header 양식 정의
#Form을 만듬
def show_form(text, msg="") :
    print("Content-Type: text/html;charset=utf-8\r\n")
    #print("")
    print("""
        <html><body><form>
        <textarea name="text" rows="8" cols="40">{0}</textarea>
        <p><input type="submit" value="WhatKind?"></p>
        <p>{1}</p>
        </form></body></html>
    """.format(html.escape(text), msg))

def detect_lang(text) :
    text = text.lower()
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [ 0 for i in range(26)]
    for ch in text:
       n = ord(ch) - code_a
       if 0 <= n < 26: cnt[n] += 1
    total = sum(cnt)
    if total == 0: return "입력이 없습니다"
    freq = list(map(lambda n: n/total, cnt))
    #언어예측
    res = clf.predict([freq])

    lang_dic = {
        "en":"english", "fr":"france", "id":"indonesia","tl":"tagalog"
    }
    return lang_dic[res[0]]

form = cgi.FieldStorage()
text = form.getvalue("text", default="")
msg=""
if text != "" :
    lang = detect_lang(text)
    msg = "kind : " + lang

show_form(text, msg)