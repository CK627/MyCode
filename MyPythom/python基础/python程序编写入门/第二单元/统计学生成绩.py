# -*- coding = utf-8 -*-
# @Time: 2021/12/219:48
# @Author： CK
# @File: 精简版.py
# @Software: PyCharm
cj=[] # 创建一个空列表
for i in range(1,7):
    zt=int(input('请输入第%d个同学的成绩:' % i))
    cj.append(zt)
print('六位同学成绩为：',cj)
print('最高分为：',max(cj))
print('最低分为：',min(cj))
print('平均分是：',sum(cj)/6)

