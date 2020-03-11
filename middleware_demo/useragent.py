# -*- coding:utf-8 -*-
__author__ = 'px'

import requests
headers = {
    "User-Agent": 'PhantomJS'
    # "User-Agent": ''
    # "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

response = requests.get('http://127.0.0.1:8000/', headers=headers)
print(response.text)
