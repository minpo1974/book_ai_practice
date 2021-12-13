'''
https://api.photozou.jp/rest/search_public.xml?keyword="牛丼"
keyword, copyright, offset, limit
https://api.photozou.jp/rest/search_public.json
'''

PHOTOZOU_API = "https://api.photozou.jp/rest/search_public.json"
CACHE_DIR = "./image/cache1"

import urllib.parse as parse
import os
import re
import json
import urllib.request as req
import time

def search_photo(keyword, offset=0, limit=100) :
    #print(keyword)
    keyword_enc = parse.quote_plus(keyword) #URL로 이동하기 위한 쿼리 문자열을 만든다.
    #print(keyword_enc)
    #keyword_unenc = parse.unquote(keyword_enc)
    #print(keyword_unenc)
    q = "keyword={0}&offset={1}&limit={2}".format(keyword_enc, offset,limit)
    #print(q)
    url = PHOTOZOU_API + "?" + q
    #print(url)

    if not os.path.exists(CACHE_DIR) :
        os.makedirs(CACHE_DIR)

    #print(url)
    '''
    re.sub(정규표현식, 대상문자열,치환문자)
    [] : 대괄호
       여러 문자 중 하나와 일치
       [와 ] 사이에 원하는 문자를 여러 개 넣으면, 넣은 문자 중 하나와 일치하면 매칭이 이루어진다.
       OR개념
       [ ] 한문자와 일치
       [abc] 'a' re.match 되었다.
       'b','c'
       'd' x
    
    ^ : 맨 앞에 사용될 경우에만, 문자 패턴이 아닌 것과 매칭
    [^a-d] : a 그리고 b 그리고 c 그리고 d가 아닌 문자열
    * : 0회이상
    + : 1회 이상
    {n,m} ,{n}, {n,}
    ?

    '''
    cache = CACHE_DIR + "/" + re.sub(r'[^a-zA-Z0-9\%\#]+','_',url)
    #cache = '010-2805-09*6!9%#^'
    #cache = re.sub(r'[%$^*!#]','',cache)
    #cache = re.sub(r'[^0-9-]','',cache)
    #print(cache)

    if os.path.exists(cache) :
        return json.load(open(cache,"r", encoding="utf-8"))
    print("[API] " + url)
    req.urlretrieve(url, cache)
    time.sleep(1)
    return json.load(open(cache,"r", encoding="utf-8"))

def download_thumb(info, save_dir) :
    if not os.path.exists(save_dir) : os.makedirs(save_dir)
    if info is None : return
    #print(info["info"])
    if not "photo" in info["info"] :
        print("[Error] broken info")
        return
    photolist = info["info"]["photo"]
    #print(photolist)
    for photo in photolist :
        title = photo["photo_title"]
        #print(title)
        photo_id = photo["photo_id"]
        #print(photo_id)
        url = photo["thumbnail_image_url"]
        #print(url)
        path = save_dir + "/" + str(photo_id) + "_thumb.jpg"
        #print(path)
        if os.path.exists(path) : continue
        try :
            print("[download", title, photo_id)
            req.urlretrieve(url,path)
            time.sleep(1)
        except Exception as e :
            print("[Error] failed to download url=", url)

def download_all(keyword, save_dir, maxphoto=1000) :
    offset = 0
    limit = 100
    while True :
        info = search_photo(keyword, offset=offset, limit=limit)
        if info is None :
            print("[Error] no result")
            return
        if (not "info" in info) or (not "photo_num" in info["info"]) :
            print("[Error] broken data")
            return
        photo_num = info["info"]["photo_num"]
        if photo_num == 0 :
            print("photo_num = 0, offset=", offset)
            return
        print("*** download offset ===> ", offset)
        download_thumb(info, save_dir)
        offset += limit
        if offset >= maxphoto :
            break

#info = search_photo("牛丼", offset=0, limit=100)
#download_thumb(info, "./image/gyudon1")
download_all("牛丼", "./image/gyudon1")
