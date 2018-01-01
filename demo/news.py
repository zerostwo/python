import requests
from bs4 import BeautifulSoup

newsurl='http://news.sina.com.cn/china/'
res=requests.get(newsurl)
res.encoding='utf-8'
soup=BeautifulSoup(res.text)
for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
        h2 = news.select('h2')[0].text
        time = news.select('.time')[0].text
        a = news.select('a')[0]['href']
        
        print(time, h2, a)


