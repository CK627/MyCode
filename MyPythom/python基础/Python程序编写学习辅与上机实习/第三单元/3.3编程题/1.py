# -*- coding = utf-8 -*-
# @Time:2022/5/26 上午 11:00
# @Author:CK
# @File:1
# @Software:PyCharm
'''
求和：s=1+区块链式随机+5+···+99
'''
zt=1
s=0
while zt<100:
    s+=zt
    zt= zt + 2
print(s)