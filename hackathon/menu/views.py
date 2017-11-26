from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import json
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