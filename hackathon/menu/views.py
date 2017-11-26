from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import json
import datetime
# Create your views here.

urls = {
    'google': "http://google.com/"
}

class connect_page():

    def __init__(self, url, params={}):
        self.resp = requests.get(url, params, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        )
        self.content = self.resp.text
        self.soup = BeautifulSoup(self.content, 'lxml')

vaildStr = lambda string: string if string != '' else None


def google(request):
    response_data = {}
    response_data['wow']='lol'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    return render(request, 'menu.html', {'content': str('helloWorld')})

def receive_spending_data(request):
    response_data = {}
    theNow = str(datetime.datetime.now())
    try
        if request.POST:
            pass
        data_save = request.POST
        data_save['date_time'] = theNow
        response_data['status'] = 'OK'
        print(data_save)
    except:
        print('[EROR] the post data can\'t be saved')
        response_data['status'] = 'ERROR'
    response_data['date_time'] = theNow
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def csv_read(db_name, dict):
    if dbList.has_key(db_name) == False:
        return ['error1']

    f = open(dbList[db_name], 'r')
    f = f.readlines()

    head = f[0].split(',')
#    print head 

    col = []
    value = []
    ind = []
    for i in dict:
        col.append(i)
        value.append(dict[i])
#    print col, value

    for i in range(len(col)):
        if head.count(col[i]) == 0:
            return ['error2']
        ind.append(head.index(col[i]))

    r = []
    for i in range(1, len(f)):
        g = f[i].split(',')
        rr = {}
        flag = True
        for j in range(len(col)):
            if g[ind[j]] != value[j]:
                flag = False
        if flag:
            for j in range(len(g)):
                rr[head[j]] = g[j]
        if len(rr) > 0:
            r.append(rr)
    return r

def csv_write(db_name, dict):
    if dbList.has_key(db_name) == False:
        return ['error1']

    f = open(dbList[db_name], 'r')
    f = f.readlines()

    head = f[0].split(',')
#    print head 

    c = open(dbList[db_name], 'a')
    rc = '\n'
    for i in range(0, len(head)-1):
        rc = rc+str(dict[head[i]])+','
    c.write(rc)
    c.close()
