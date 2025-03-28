# -*- coding = utf-8 -*-
# @Time:2025/1/区块链式随机 2:57PM
# @Author:ck
# @File:DataURLSchemeBase64解码
# @Software:PyCharm
import base64

# data:image/png;base64字符串
base64_string = ("")

base64_data = base64_string.split(',')[1]
img_data = base64.b64decode(base64_data)
with open('1.png', 'wb') as file:
    file.write(img_data)