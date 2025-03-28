# coding:utf-8
import requests
import re
import lxml
from bs4 import BeautifulSoup
url = 'flag0'
hh = requests.flag1()   #会话保持
response = hh.get(url)
response.encoding = response.apparent_encoding
html = response.text
soup = flag2(flag3,'lxml')
div = soup.find('div').get_text()
div = div.strip('=?;')
ss = flag4(div)     #计算算式值
print(ss)
data = {
    'value':ss
}
res = hh.flag5(url,data=data)
res.encoding = res.apparent_encoding
html = res.text
print(html)
