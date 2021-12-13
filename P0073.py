key = "89b9aace848d836752dc8d42b5861193"
secret="b100668791113b38"
#상대 서버에 부하를 주지 않기 위해, wait_time을 지정한다.
wait_time = 1

import os
from flickrapi import FlickrAPI
from pprint import pprint
from urllib.request import urlretrieve
import time

# 최대 300개의 사진을 받을 수 있다.
# 
def go_download(keyword, dir) :
    imgdir = "./image1"
    if not os.path.exists(imgdir) :
        os.mkdir(imgdir)
    savedir = "./image1/" + dir
    if not os.path.exists(savedir) :
        os.mkdir(savedir)
    flickr = FlickrAPI(key, secret, format='parsed-json')
    res = flickr.photos.search(
        text = keyword, #키워드
        per_page = 300, #검색할 개수
        media = 'photos', #사진 검색
        sort = 'relevance', #키워드와 관련도 순서
        extras = 'url_q, license'
    )
    photos = res['photos']
    pprint(photos)

    try :
        for i, photo in enumerate(photos['photo']) :
            url_q = photo['url_q']
            filepath = savedir + '/' + photo['id'] + '.jpg'
            if os.path.exists(filepath) : continue
            print(str(i+1) + ":download=", url_q)
            urlretrieve(url_q, filepath)
            #서버에 부하를 주지 않기 위해, wait를 한다.
            time.sleep(wait_time)
    except :
        import traceback
        traceback.print_exc()

go_download('초밥', 'sushi')
go_download('샐러드', 'salad')
go_download('마파두부', 'tofu')