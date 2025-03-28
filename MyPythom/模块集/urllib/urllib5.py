# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月11日
"""
data = {
    'first': 'true',
    'pn' : 1,
    'kd' : 'Python'
}
proxy =request.ProxyscHandler({'http:' 5.22.195.215.4})    #设置proxy
opener = request.build__opener(proxy)    #挂载opener
request.install_opener(opener) #安装opener
data = parse.urlencode(data).encode('utf-8')
page = opener.open(url,data).read()
page = page.ecode('utf-8')
return page

