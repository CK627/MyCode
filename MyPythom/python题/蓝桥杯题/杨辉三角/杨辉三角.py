# -*- coding = utf-8 -*-
# @Time: 2021/12/1317:48
# @Author： CK
# @File: 杨辉三角
# @Software: PyCharm
'''
蓝桥杯省赛：给定一个正整数N，请你输出在杨辉三角中第一次出现N是在第几个数?
'''
while True:
    triangle = []
    triangle1 = []
    n = int(input('请输入一个整数：'))
    if n==0:
        break
    for i in range(n):
        cur = [1]
        if i == 0:
            triangle.append(cur)
            continue
        for j in range(i - 1):
            cur.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        cur.append(1)
        triangle.append(cur)
    print(triangle)
    triangle1.extend(str(triangle))
    print(triangle1)
    try:
        x=int(input('请输入一个整数：'))
        if x in triangle1:
            print(len(triangle1))
    except:
        print('范围太小无法找到')