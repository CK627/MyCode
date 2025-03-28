# -*- coding = utf-8 -*-
# @Time: 2022/1/616:10
# @Author： CK
# @File: 回文判断
# @Software: PyCharm
while True:
    zt=input('请输入要判断的内容（-1退出）：')
    b = zt[::-1]
    if zt== '-1':
        break
    if zt==b:
        print(zt, '回文')
    else:
        print(zt, '不是回文')