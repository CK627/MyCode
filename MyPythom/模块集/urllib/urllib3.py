# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月11日
"""
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}
data = parse.urlencode(data).encode('utf-8')