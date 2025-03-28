
import re
from urllib import request
# '''网址'''  图片_百度百科  获取整个网页的代码
url = 'http://172.16.1.7:999'
page = request.urlopen(url)
code = page.read()
code=code.decode('utf-8')
 
# 正则表达式  编译
pattern = 'src="(.+\.bmp)"'
reg = re.compile(pattern)
 
# 找到图片资源并下载到指定目录
imgs = reg.findall(code)
i = 0
for img in imgs:
    i = i + 1
    print(str(i)+img)
    request.urlretrieve(img,r'C:\Users\mask\Desktop\aa\133232\%s.jpg' %i)