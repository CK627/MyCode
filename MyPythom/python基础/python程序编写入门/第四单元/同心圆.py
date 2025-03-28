# -*- coding = utf-8 -*-
# @Time: 2022/1/415:49
# @Author： CK
# @File: 同心圆
# @Software: PyCharm
import turtle
try:
    RGB=[]
    while True:
        print('输出’退出‘后按换行键会停止本次循环')
        zt=input('请设置你需要的颜色（注：你的颜色数量决定了你要画多少圆）：')
        if zt== '退出':
            break
        else:
            RGB.append(zt)
    r=int(input('请输入第一个圆的初始半径:'))
    for i in range(len(RGB)):
        turtle.penup() # 拿起笔
        turtle.goto(0,-r-20*i) # 转动到或者移动到某个位置
        turtle.pendown() #
        turtle.color(RGB[i])
        turtle.circle(r+20*i)
    turtle.done()
except:
    print('请按照要求输入')