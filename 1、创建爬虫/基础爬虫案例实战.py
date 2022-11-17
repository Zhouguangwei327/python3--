import json
import requests
import logging
import re
import multiprocessing
import datetime
from urllib.parse import urljoin
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULTS_DIR = 'results'
exists (RESULTS_DIR) or makedirs(RESULTS_DIR)



# 公共获取页面html
def scrape_page(url):
    logging.info('scraping {} ...'.format(url))
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code:{} while scraping {}'.format(response.status_code, url))
    except Exception as e:
        logging.error(e)

# 获取首页html
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


# 获取首页html中详情页的的url
def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url: {}'.format(detail_url))
        yield detail_url


# 循环获取所有详情页的url
def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data: {}'.format(data))
        logging.info('save data to json file')
        save_data(data)
        logging.info('saved successfully')


# 获取详情页的html
def scrape_detail(url):
    return scrape_page(url)


# 解析详情页的html
def parse_detail(html):
    try:
        # 名称
        movie_name = re.search('<h2.*?class.*?>(.*?)\s-\s.*?</h2>', html).group(1)
        # movie_name = movie_name.group(1)

        # 封面
        movie_cover_url = re.search('class="item.*?<img.*?src="(.*?)".*?class="cover">', html, re.S).group(1)


        # 上映时间
        movie_showtime = re.search('<span.*?>(.*?)\s上映</span>', html).group(1)
 

        # 评分
        # score_parttern = re.compile('<p\s.*?score.*?>(.*?)</p>', re.S)
        movie_score = re.search('<p\s.*?score.*?>\s{15}(.*?)</p>', html, re.S).group(1)
 
        # 剧情简介
        movie_synopsis = re.search('<div.*?drama.*?>.*?<p.*?>\s{19}(.*?)\s{17}</p>', html, re.S).group(1)

        json_file = {
            "movie_name": movie_name,
            "movie_cover_url": movie_cover_url,
            "movie_synopsis": movie_synopsis,
            "movie_showtime": movie_showtime,
            "movie_score": movie_score
        }
    except Exception as e:
        logging.error(e)
        json_file = {
            "movie_name": "movie_name",
            "movie_cover_url": 'movie_cover_url',
            "movie_synopsis": 'movie_synopsis',
            "movie_showtime": 'movie_showtime',
            "movie_score": 'movie_score'
        }

    
    return json_file


def save_data(data):
    name = data['movie_name']
    data_path = f'{RESULTS_DIR}/{name}.json'
    data = json.dumps(data, ensure_ascii=False, indent=2)
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(data)



if __name__ == '__main__':
    start_time = datetime.datetime.now()
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE+1)
    pool.map(main, pages)
    pool.close()
    pool.join()
    end_time = datetime.datetime.now()
    print(end_time - start_time)

