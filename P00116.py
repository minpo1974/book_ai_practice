from bs4 import BeautifulSoup as bs
import urllib.request
import re
from pandas.core.algorithms import mode
from requests.api import head
from selenium import webdriver
import pandas as pd
import datetime
import os
import getpass

def get_URL(page) :
    url_before_page ="http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=machine+learing&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount="
    url_after_page = "&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D"

    URL = url_before_page + page + url_after_page
    #print(URL)
    return URL

def get_reference(URL) :
    #driver_path = os.path.join(ROOT_PATH, "chromdriver")
    driver = webdriver.Chrome(executable_path='D:/test/chromedriver_win32/chromedriver.exe',options=webdriver.ChromeOptions().add_argument("headless"))
    driver.get(URL)

    html = driver.page_source
    soup = bs(html, "html.parser")
    title = soup.find("h3", "title")
    title_txt = title.get_text("",strip=True).split("=")
    title_kor = re.sub("\n\b","", str(title_txt[0]).strip())
    #print(title_kor)
    print("title_txt : ", title_txt)
    if len(title_txt) > 2 : 
        title_eng = str(title_txt[1]).strip()
    else :
        title_eng = "None"

    txt_box = []
    for text in soup.find_all("div","text") :
        txt = text.get_text("", strip=True)
        txt_box.append(txt)

    txt_kor = txt_box[1]
    if len(txt_box) > 3 : 
        txt_eng = txt_box[3]
    else :
        txt_eng = "None"

    detail_box = []
    detail_info = soup.select(
        "#soptionview > div > div.thesisInfo > div.infoDetail.on > div.infoDetailL > ul > li > div > p"
    )
    for detail in detail_info :
        detail_content = detail.get_text("", strip=True)
        detail_wrap = []        
        detail_wrap.append(detail_content)        
        detail_box.append(detail_wrap)
    author = ",".join(detail_box[0])
    book = (
        "".join(detail_box[2] + detail_box[3]).replace("\n","").replace("\t","").replace(" ","")
        + " p."
        + "".join(detail_box[-2])
    )
    keyword = ",".join(detail_box[6])
    reference_data = pd.DataFrame(
        {
            "저자" : [author],
            "국문 제목" : [title_kor],
            "영문 제목" : [title_eng],
            "수록지" : [book],
            "핵심어" : [keyword],
            "국문 요약" : [txt_kor],
            "링크" : [URL],
        }
    )

    driver.close()
    return reference_data

def save_csv(csv_path, data) :
    csv = csv_path.replace("/","\\")   
    #print(csv_path) 
    if os.path.isfile(csv_path):
        print(data['저자'])
        print(data['국문 제목'])
        print(data['영문 제목'])
        print(data['수록지'])
        print(data['핵심어'])
        print(data['국문 요약'])
        print(data['링크'])
        data.to_csv(csv, mode='a', header=False, index=False, encoding="utf-8")
        #data.to_csv(csv, mode='a', header=False, index=False, encoding="euc-kr")
        #data.to_csv(csv, mode='a', header=False, index=False, encoding="utf-8-sig")
        #data.to_csv(csv, mode='a', header=False, index=False, encoding="ms-949")
        #data.to_csv(csv, mode='a', header=False, index=False, encoding="utf-8")
    else :
        print(data['저자'])
        print(data['국문 제목'])
        print(data['영문 제목'])
        print(data['수록지'])
        print(data['핵심어'])
        print(data['국문 요약'])
        print(data['링크'])        
        data.to_csv(csv, mode='w', header=True, index=False, encoding="utf-8")
        #data.to_csv(csv, mode='w', header=True, index=False, encoding="euc-kr")
        #data.to_csv(csv, mode='a', header=False, index=False, encoding="utf-8-sig")
        #data.to_csv(csv, mode='a', header=False, index=False, encoding="ms-949")
        #data.to_csv(csv, mode='a', header=True, index=False, encoding="utf-8")

def get_link(csv_name, page_num) :
    for i in range(page_num) :
        current_page = i*10
        URL = get_URL(str(current_page))
        source_code_from_URL = urllib.request.urlopen(URL)
        soup = bs(source_code_from_URL, 'lxml', from_encoding='utf-8')

        for j in range(10) :
            paper_link = soup.select('li > div.cont > p.title > a')[j]['href']
            paper_url = "http://riss.or.kr" + paper_link
            print(paper_url)
            reference_data = get_reference(paper_url)
            save_csv(csv_name, reference_data)


get_link("./minpo.csv",1)