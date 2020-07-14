#pip install --upgrade pip 진행후
from selenium import webdriver    #pip install selenium
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup   #pip install bs4
import time 
from konlpy.tag import Kkma  #pip install konlpy
import openpyxl    #pip install openpyxl  #엑셀에 저장하기
#라이브러리 불러오기
 
kma = Kkma()
 
excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
#엑셀 파일로 저장하기 위한 작업 start
 
chromedriver ='chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
#selenium 라이브러리 기본 작업


driver.get('https://everytime.kr/login')
#크롤링 할 홈페이지 가져오기
driver.find_element_by_name("userid").send_keys("아이디")
#태그의 네임이 userid 인 element 가져오고 "아이디" 입력
driver.find_element_by_name("password").send_keys("비밀번호")
#태그의 네임이 password 인 element 가져오고 "비밀번호" 입력
driver.find_element_by_tag_name("input").send_keys(Keys.RETURN)
#로그인 버튼 찾고 클릭
 
#time.sleep(2)
#driver.get('https://everytime.kr/418861')  #동아리.학회 게시판으로 이동

time.sleep(2)
driver.find_element_by_xpath('//*[@id="submenu"]/div/div[1]/a').click()


time.sleep(3)
driver.find_element_by_xpath('//*[@id="sheet"]/ul/li[3]/a').click()
# 2페이지에 뜨는 광고창 1번 끄기

def next_page():
    time.sleep(0.5)
    
    res = driver.page_source
    soup = BeautifulSoup(res,"html.parser")
    data_title = soup.select('#container > div.wrap.articles > article > a > h2')
    data_text = soup.select('#container > div.wrap.articles > article > a > p')
    data_url = soup.select('#container > div.wrap.articles > article > a')
    data_date = soup.select('#container > div.wrap.articles > article > a > time')
#함수 next_page 생성, 핫 게시판에서 (공감수, 제목, 내용, url) 찾고 저장할 준비
    
    for title,text,url,date in zip(data_title,data_text,data_url,data_date):
        excel_sheet.append([title.get_text(),text.get_text(),'https://everytime.kr'+url.get('href'),date.get_text()])       
#name,text,url 이라는 폴더에 (제목, 내용, url, 작성일) 각각 넣고 튜플로 저장

    driver.find_element_by_css_selector('#container > div.wrap.articles > div.pagination > a.next').click()

 
time.sleep(0.5)
for page_roof in range(3):
    next_page()
# next_page를 page_roof라는 폴더에 넣고 30번 반복
 
excel_file.save('everytime crawling.xlsx')
# everytime crawing 라는 엑셀 파일에 저장 
excel_file.close()
    
driver.quit()

