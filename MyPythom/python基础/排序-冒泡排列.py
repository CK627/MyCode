# -*- coding = utf-8 -*-
# @Time: 2021/12/2910:21
# @Author： CK
# @File: 排序-冒泡排列
# @Software: PyChar
ls=[]
while True:
    zt=input('请输入一个整数,输入退出换行终止本次循环：')
    if zt== '退出':
        break
    else:
        ls.append(int(zt))
n=len(ls)
for i in range(n):
    for j in range(0,n-i-1):
        if ls[j]>ls[j + 1]:
            ls[j], ls[j + 1]= ls[j + 1], ls[j]
print('排序后的数组：', ls)
