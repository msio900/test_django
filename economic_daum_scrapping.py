import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

# conn = sqlite3.connect('db.sqlite3')
# query = 'CREATE TABLE economic (title TEXT, link TEXT, create_date datetime)'
# conn.execute(query)
# conn.commit()
# conn.close()
res = requests.get('http://media.daum.net/economic/')
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a', class_='link_txt')
    print('task_crawling_daum : ', type(links), len(links))
    with sqlite3.connect("db.sqlite3") as con:
        cur = con.cursor()
        title = str()
        link = str()
        for link in links:
            title = str.strip(link.get_text())
            link = link.get('href')
            try:
                cur.execute(
                    "INSERT INTO economic (title,link,create_date) VALUES (?,?,?)", (title, link, datetime.datetime.now()))
            except :
                pass
        con.commit()
