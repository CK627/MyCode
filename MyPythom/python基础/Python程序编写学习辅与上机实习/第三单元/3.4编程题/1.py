# -*- coding = utf-8 -*-
# @Time:2022/6/23 下午 7:57
# @Author:CK
# @File:1
# @Software:PyCharm
'''
小明17岁生日时种3棵树，以后每天过年生日都去种树，并且每年都比前一年多种两棵数，那么小明多少岁可以种不少于100棵数？变量命名建议：小明年龄为age，当前种树的数为tree，树的总和为trees。程序运行结果如下。
小明26岁可以种树120棵树
'''
age=17
tree=3
trees=0
while True:
    age=age+1
    tree=tree+2
    trees+=tree
    if trees>100:
        break
print("小明",age,"岁可以种树",trees+3,"棵树")