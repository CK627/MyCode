# -*- coding = utf-8 -*-
# @Time: 2021/12/1317:48
# @Author： CK
# @File: 杨辉三角
# @Software: PyCharm
"""
蓝桥杯省赛：给定一个正整数N，请你输出在杨辉三角中第一次出现N是在第几个数?
"""


triangle = []
n = int(input('请输入一个整数：'))
for i in range(n):
    cur = [1]
    if i == 0:
        triangle.append(cur)
        continue
    for j in range(i - 1):
        cur.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
    cur.append(1)
    triangle.append(cur)
# print(triangle)

c=0 #计数器，用于统计第几个数与N相等
f=False #找到N的标志
for i in triangle: #把杨辉三角的每一行提取出来
    for j in range(len(i)):
        c=c+1 #每检查一个数，计数器就加1
        if i[j]==n: #找到数，退出循环
            f=True
            break
    if f:
        break
print(c)
            




