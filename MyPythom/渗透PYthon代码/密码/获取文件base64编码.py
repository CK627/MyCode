# -*- coding = utf-8 -*-
# @Time:2023/10/12 18:50
# @Author:ck
# @File:获取文件base64编码
# @Software:PyCharm
import base64
f = open(r'/Users/ck/Documents/MyCode/Python/1/获取图片base64编码.py','rb').read()
s = base64.b64encode(f)
print(s)