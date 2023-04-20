#!/usr/bin/env python3
#coding:utf-8

import requests

def testRequests():
    r = requests.get('https://www.douban.com/')
    print(r.status_code)

    r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
    print(r.url)
    print(r.encoding)
    print(r.content)
