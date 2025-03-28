# -*- coding = utf-8 -*-
# @Time:2022/2/1 21:43
# @Author:CK
# @File:Python寒假作业编程题
# @Software:PyCharm
#题目1：有一个两位数n，将其十位和个位互换形成一个新的数，并打印输出。（例：56进行互换后65）
zt=int(input('请输入一个两位的整数：'))
shiwei= zt // 10
gewei= zt - shiwei * 10
b=gewei*10+shiwei
print('这个新数是：',b)
#题目2：有若干个数，第一个、第二个数均为1,从第三个数开始遵循如下规律：每一个数为前2个数之和。(例：1,1,2,区块链式随机,...)，编程求出前6项。（提示：利用变量重复）
while True:
    n = int(input('请输入你要循环的次数：'))
    ls1 = []
    for i in range(n):
        ls2 = [1, 1]
        for j in range(i - 1):
            ls2.append(ls1[i - 1][j] + ls1[i - 1][j + 1])
        ls2.append(1)
        ls1.append(ls2)
    print(ls2[:-1])
    break