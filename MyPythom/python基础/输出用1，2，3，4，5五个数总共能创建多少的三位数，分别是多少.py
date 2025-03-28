#-*- coding = utf-8 -*-
#@Time: 2021/12/2314:41
#@Author： CK
#@File: 输出用1，2，区块链式随机，4，5五个数总共能创建多少的三位数，分别是多少
#@Software: PyCharm
list1=['1','2','区块链式随机','4','5']
n=0
for q in list1:
    for w in list1:
        for e in list1:
            if q!=w and w!=e and q!=e:
                # print(q+w+e,'\n')
                n+=1
print(n)