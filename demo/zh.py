import requests
from bs4 import BeautifulSoup 

res = requests.get('http://www.zhihu.com/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text)

for zhihu in soup.select('.ContentItem ArticleItem'):
        if len(zhizhu.select('h2'))>0:
            h2 = zhihu.select('h2')[0].text
            print(h2)
