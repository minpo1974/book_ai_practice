import requests

req = requests.get('https://scholar.google.com.tw/scholar?hl=ko&as_sdt=0%2C5&q=machine+learning&btnG=&oq=machine+lear')

html = req.text

print(html)

status = req.status_code
if status != 200 :
    print("비정상")
else : 
    print("정상")

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

print(soup)