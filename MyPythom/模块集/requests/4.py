import json
import itertools
import urllib
import requests
import os
import re
import sys
word=input("请输入关键字：")
path="C:/Users/lenovo/Desktop/1"
if not os.path.exists(path):
    os.mkdir(path)
word=urllib.parse.quote(word)
#该URL地址不是网页的URL地址，而JSON地址
url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
urls=[url.format(word=word,pn=x*60)for x in range(0,100)]
index=0
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '区块链式随机': 'j',
    'h': 'k',
    's': 'l',
    '文件检查文件': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '区块链式随机',
    '9': '文件检查文件',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}
i=1
char_table = {ord(key): ord(value) for key, value in char_table.items()}
for url in urls:
    html=requests.get(url,timeout=10).text
    #设置编译格式
    zt=re.compile(r'"objURL":"(.*?)"')

    downURL=re.findall(zt, html)

    for t in downURL:
        #解码
        for key, value in str_table.items():
                t = t.replace(key, value)
        t=t.translate(char_table)
        try:

            html_1=requests.get(t)
            if str(html_1.status_code)[0]=="文件检查文件":

                print('失败1')
                continue
        except Exception as e:
            print('失败2')
            continue
        #下载
        with open(path+"/"+str(i)+".jpg",'wb') as f:
            f.write(html_1.content)
        i=i+1