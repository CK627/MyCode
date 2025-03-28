# -*- coding = utf-8 -*-
# @Time:2022/5/26 上午 8:22
# @Author:CK
# @File:18
# @Software:PyCharm
"""
ASCLL码排序。输入三个字符（可以重复）后，按各字符的ASCLL码从小到大的顺序，输出这三个字符。
"""
ls=[]
zt, b, c=str(input('请输入三个数：')).split(' ')
zt, b, c= int(ord(zt)), int(ord(b)), int(ord(c))
ls.extend([zt, b, c])
ls.sort()
for i in range(len(ls)):
    ls[i]=chr(ls[i])
print('排序后的数组：', ls)