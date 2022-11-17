import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center/'
html = requests.get(url=url).text
doc  =pq(html)
items = doc('.el-card').items()


file = open('movie.txt', 'w', encoding='utf-8')

for item in items:
    # 电影名称
    name = item.find('a > h2').text()
    file.write(f'名称：{name}')
    file.write
file.close()