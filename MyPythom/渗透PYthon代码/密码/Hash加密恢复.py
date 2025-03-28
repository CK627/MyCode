# -*- coding = utf-8 -*-
# @Time:2023/10/12 18:37
# @Author:ck
# @File:Hash加密恢复
# @Software:PyCharm
import hashlib
import itertools
key = 'c2979c7124'
dir = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dir_list = itertools.product(dir, repeat=4)
for i in dir_list:
    res = hashlib.md5(''.join(i).encode()).hexdigest()
    if res[0:10] == key:
        print(i)
        print(res)