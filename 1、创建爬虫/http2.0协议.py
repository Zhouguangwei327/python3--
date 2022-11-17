from textwrap import indent
import requests
import logging
import re
import json
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')




TOTAL_PAGE = 1
requrest = requests.session()
BASE_URL = 'https://ssr1.scrape.center'
while TOTAL_PAGE <= 10:
    page_url = f'{BASE_URL}/page/{TOTAL_PAGE}'
    res = requrest.get(page_url)
    html = res.text
    # print(html)
    TOTAL_PAGE += 1


    detail_pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    detail_uris = re.findall(detail_pattern, html)

    for detail_uri in detail_uris:
        detail_url = f'{BASE_URL}{detail_uri}'

        detail_res = requrest.get(detail_url)
        detail_html = detail_res.text

        try:
            # 名称
            movie_name = re.search('<h2.*?class.*?>(.*?)\s-\s.*?</h2>', detail_html).group(1)
            # movie_name = movie_name.group(1)

            # 封面
            movie_cover_url = re.search('class="item.*?<img.*?src="(.*?)".*?class="cover">', detail_html, re.S).group(1)
            movie_cover = requrest.get(movie_cover_url)


            # 上映时间
            movie_showtime = re.search('<span.*?>(.*?)\s上映</span>', detail_html).group(1)


            # 评分
            # score_parttern = re.compile('<p\s.*?score.*?>(.*?)</p>', re.S)
            movie_score = re.search('<p\s.*?score.*?>\s{15}(.*?)</p>', detail_html, re.S).group(1)

            # 剧情简介
            movie_synopsis = re.search('<div.*?drama.*?剧情简介.*?"">\s{19}(.*?)\s{17}</p></div>', detail_html,re.S).group(1)

            json_file = json.dumps({
                "movie_name": movie_name,
                "movie_cover_url": movie_cover_url,
                "movie_score": movie_score,
                "movie_showtime": movie_showtime,
                "movie_synopsis": movie_synopsis
            }, ensure_ascii=False, indent=2)

            print(json_file)

            with open(f'{movie_name}.json', 'w', encoding='utf-8') as file:
                file.write(json_file)
        except Exception as e:
            logging.error(e)





    


