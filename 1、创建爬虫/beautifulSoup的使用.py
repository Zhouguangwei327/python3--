from bs4 import BeautifulSoup
import scrapy

soup = BeautifulSoup(open('./test.html'), 'lxml')
print(soup.select('#link1'))