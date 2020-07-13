import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('span.item_title')
i=1
f = open("네이버 실시간 검색어 순위.txt", "w")
for item in data:
    data = str(i) + "위 : " + item.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()