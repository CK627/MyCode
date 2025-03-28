# coding:utf-8
import requests
import re
import lxml
from bs4 import BeautifulSoup
url = 'http://1.1.1.1/zkpy/zkpy.php'
hh = requests.session()   #定义一个http连接（会话）的对象，类似定义一个变量
response = hh.get(url)
response.encoding = response.apparent_encoding
html = response.text
soup = BeautifulSoup(html,'lxml')
div = soup.find('div').get_text()
div = div.strip('=?;')
ss = eval(div)     #计算算式值
print(ss)
data = {
    'value':ss
}
res = hh.post(url,data=data)
res.encoding = res.apparent_encoding
html = res.text
print(html)