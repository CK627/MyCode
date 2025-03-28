# -*- coding = utf-8 -*-
# @Time: 2022/1/615:34
# @Author： CK
# @File: 韩信点兵求人数
# @Software: PyCharm
# print('韩信点兵求人数：')
# print('规则：三三数之剩二，五五数之剩四，七七数之剩六')
n=1000
while True:
    if n%3==2 and n%5==4 and n%7==6:
        break
    else:
        n=n+1
print('士兵有：',n,'人')