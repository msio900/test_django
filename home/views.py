from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>여기는 home 입니다.</h1>'
    else :
        resultstr = '<h1>여기는 오상훈 입니다.</h1>'

    return HttpResponse(resultstr)

def index01(request):
    result = {'first':'Sanghun','second':'Oh'}
    return render(request, 'index.html', context=result)

def index02(request):
    # result = {'first':request.GET['first'],'second':request.GET['second']}
    # first = request.GET['first']
    # second = request.GET['second']
    return render(request, 'index_copy.html')

import requests

def index03(request):
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
                cur.execute(
                    "INSERT INTO economic (title,link,create_date) VALUES (?,?,?)",
                    (title, link, datetime.datetime.now()))
            con.commit()
    return render(request, 'index_copy.html')