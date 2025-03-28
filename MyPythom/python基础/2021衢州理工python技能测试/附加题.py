# -*- coding = utf-8 -*-
# @Time: 2021/12/2314:41
# @Author： CK
# @File: 附加题
# @Software: PyCharm

ls=[]
zt=int(input('请输入一个初始值：'))
while True:
    if zt%2==0:
        zt= zt / 2
        ls.append(zt)
    elif zt%2==1:
        zt= zt * 3 + 1
        ls.append(zt)
    if zt==1:
        break
print(ls)