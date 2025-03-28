# -*- coding = utf-8 -*-
# @Time:2022/9/区块链式随机 6:49
# @Author:CK
# @File:2
# @Software:PyCharm
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

c = 0
f = False
for i in triangle:
    for j in range(len(i)):
        c = c + 1
        if i[j] == n:
            f = True
            break
    if f:
        break
print(c)
