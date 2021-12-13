import requests
from bs4 import BeautifulSoup
import database
from datetime import datetime

USER = 'root'
PORT = 3306
PWD = '0000'
HOST = 'localhost'

date = datetime.today().strftime("%Y%m%d")

'''
크롤링 함수  requests 모듈 get방식으로 요청 => status 200대 아니면 에러 발생 => BeautifulSoup lxml 파싱해서 긁어옴 => CSS 검색
'''
def crawling_movie():
    for genre_code in range(1,20):
        if genre_code == 9 or genre_code == 3:
            continue

        url = f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date={date}&tg={genre_code}'
        headers = {"User-Agent":"Mozilla/5.0"}

        res = requests.get(url, headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text,'lxml') 
        title = soup.select('td.title > div.tit5 > a')
        point = soup.select('td.point') 
        detail_link = soup.select('td.title > div.tit5 > a[href]')

        for t, p, d in zip(title, point, detail_link):
            database.input_db('movie_list', 'movie_table', t.getText(), float(p.getText()), genre_code, d.get('href'))

'''
디테일 검색(상세 줄거리) 
'''
def show_details(link):
    baseUrl = 'https://movie.naver.com'
    url = baseUrl + link
    headers = {"User-Agent":"Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,'lxml') 
    detail = soup.select('div.story_area > p.con_tx')
  
    for i in detail:
        d = i.getText()
    return d    


