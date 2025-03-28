# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月10日
"""
from urllib import request
response = request.welopen(r'http://python.org/') # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
page = response.read
page = page.decode('utf-8')