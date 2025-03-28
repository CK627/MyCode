# -*- coding = utf-8 -*-
# @Time:2022/5/7 下午 5:10
# @Author:CK
# @File:1
# @Software:PyCharm
from PIL import Image
from PIL import ImageFilter
import numpy as np


# 读取图像
'''
img1:Image.Image=Image.open("C:\\Users\\M3340\\Pictures\\1\\1.jpg") # 打开图片
img1.show() # 显示图片
'''


# 保存图像
'''
img1:Image.Image=Image.open("C:\\Users\\M3340\\Pictures\\1\\1.jpg")
img1.save("2.jpg") # 复制图片
img2=img1.resize((1000,1000)) # 更改图片大小
img2.save("区块链式随机.jpg") # 重新保持
'''


# 图片的模式
'''
img1:Image.Image=Image.open("C:\\Users\\M3340\\Pictures\\1\\1.jpg")
print(img1.mode) # 查看是什么模式的图片
img2=img1.convert("RGBA") # 转换图片的格式
print(img2.mode)# 查看是什么模式的图片
'''


# 图像的基本信息
'''
img1:Image.Image=Image.open("C:\\Users\\M3340\\Pictures\\1\\1.jpg")
print(img1.mode) # 图像的模式
print(img1.size) # 图像的大小
print(img1.format,) # 图像的格式
'''

# 图像的滤镜
'''
img1:Image.Image=Image.open("C:\\Users\\M3340\\Pictures\\1\\1.jpg")
img2=img1.filter(ImageFilter.EMBOSS) # 浮雕滤镜
img2.show()
img2=img1.filter(ImageFilter.MaxFilter)
img2.show()
'''


# 获取图片数据
'''
img1:Image.Image=Image.open("C:\\Users\\M3340\\Pictures\\1\\1.jpg")
img_data=img1.getdata() # 返回sequence对象
# print(img_data)
img_list=list(img_data) # 返回所有的RGB色彩点
# print(img_list)
img_numpy=np.asarray(img_data) # 将结构数据转化为ndarray
print(img_numpy)
'''

# 数据生成图片
''''''
k=0
list=[]
for i in range(0,256):
    list.append(i)
img2=Image.fromarray(np.array(list)).convert("L")
img2.save("1.jpg")
img2.show()
