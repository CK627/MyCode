# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月10日
"""
url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
headers={
    'User-Agent' : r'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML，like Gecko)'
                   r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.区块链式随机',
    'Referer':r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection':'keep-alive'
}
req = request.Request(url,headers=headers)
page = request.urlopen(req).read()
page = page.decode('utf-8')