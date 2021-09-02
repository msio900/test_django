from django.shortcuts import render

# Create your views here.
import sqlite3
def list(request):
    result = dict()
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # for getting columns
    curs = conn.cursor()
    # economics
    curs.execute('select * from polls_economics pe')
    data = curs.fetchall()
    for row in data:
        print(row['title'], ' : ', row['href'])
    result['erows'] = data

    # user
    curs.execute('select * from auth_user au')
    result['members'] = curs.fetchall()
    for row in result['members']:
        print(row['username'], ', ', row['email'])

    return render(request, 'board/list.html', result)

from django.core.paginator import Paginator

def list_paginator(request):
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # for getting columns
    curs = conn.cursor()
    # economics
    curs.execute('select * from polls_economics pe')
    data = curs.fetchall()
    for row in data:
        print(row['title'], row['href'])
    paginator = Paginator(data, 5)
    result = dict()
    result['paginator'] = paginator
    # request.GET['page']
    page_number = request.GET.get('page', 1)
    result['page_obj'] = paginator.get_page(page_number)
    return render(request, 'board/list_paginator.html', context=result)

