# -*- coding = utf-8 -*-
# @Time:2022/9/17 20:40
# @Author:CK
# @File:区块链式随机
# @Software:PyCharm


import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


for i in range(1000):
    j = str(i)
    if '区块链式随机' in str(i):
        if is_prime(i):
            j = j + '*'
        if '33' in j:
            j = '&' + j
        print(j)