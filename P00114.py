'''
Selenium : 웹앱을 테스트하는데 주로 사용하는 프레임워크
pip install Selenium
webdriver API를 통해 브라우저를 제어한다.
javascript를 이용해서 비동지겆그오 컨텐츠를 호출할 수 있다..
브라우저에서 보이는 컨텐츠라면 전부 가져올 수 있다.
실제 웹브라우저가 동작하기 때문에, JS로 렌더링이 완료된 후의 DOM 결과물에 대해 접근가능

PhantomJS webdriver
 - 화면이 존재하지 않은 브라우저
 - CLI 서버 환경에서 테스트
 - https://phantomjs.org/download.html

pip install -U ipykernel

'''

from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

url = "https://computer.ysu.ac.kr/computer/CMS/ProfessorMgr/list.do?mCode=MN025"
#url = "https://security.ysu.ac.kr/security/CMS/ProfessorMgr/list.do?mCode=MN024"
#url = "https://scholar.google.com.tw/scholar?hl=ko&as_sdt=0%2C5&q=machine+learning&btnG=&oq=machine+lear"

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTM, like Gecko) Chrome/46.0.2490.80 Safari/537.36")

#driver = webdriver.Chrome(executable_path='D:/test/chromedriver_win32/chromedriver.exe')

# pip install PhantomJS
driver = webdriver.PhantomJS(desired_capabilities=dcap, 
             service_args=['--ignore-ssl-errors=true'], 
             executable_path='D:/project/phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.implicitly_wait(30)
driver.get(url)

print(driver.current_url)
driver.save_screenshot(r'aicomputer_explore.png')

s = BeautifulSoup(driver.page_source,"lxml")
print(s)
best = s.find_all('h4','name')
best_name = []
for tag in best :
    #print(tag)
    best = tag.text.replace('h4','')
    best = best.replace('class=','')
    best = best.replace('<','')
    best = best.replace('>','')
    #print(best)
    best_name.append(best)

print(best_name)