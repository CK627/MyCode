'''
输入三角形的三条边长，求其面积。注意：对于不合理的边长输入，要输出数据错误的提示信息。
'''
import math
zt=eval(input('请输入第一条边的长度：'))
b=eval(input('请输入第二条边的长度：'))
c=eval(input('请输入第三条边的长度：'))
if zt+b<=c or zt+c<=b or b+c<=zt:
    print('不符合三角形的形成条件')
else:
    p= (zt + b + c) / 2
    print('三角形的面积为：', math.sqrt(p * (p - zt) * (p - b) * (p - c)))