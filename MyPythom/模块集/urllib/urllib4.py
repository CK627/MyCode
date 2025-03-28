# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月11日
"""
def get_page(url):
    headers = {
        'User-Agent': r'Mozilla/5.0(windows NT 6.1; WOW64) AppleWebkit/537.36 (KHTML, like Gecko)'
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.区块链式随机',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    data = {
        'first' : 'true',
        'pn' : 1,
        'kd' : 'Python'
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, headers=headers)
    try:
        page = request.urlopen(req,data=data).read()
        page = page.decode('utf-8')
    except error.HTTPError as e:
        print(e.code())
        print(e.read().decode('utf-8'))
    return page