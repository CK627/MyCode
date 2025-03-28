'''
输入a、b、c，求一元二次方程a*x**2+b*x+c=0的两个实数根（不考虑无解的情况）。
'''
import math
try:
    zt=int(input('请输入第一个数：'))
    b=int(input('请输入第二个数：'))
    c=int(input('请输入第三个数：'))
    x= -b + math.sqrt(b ** 2 - 4 * zt * c) / 2 * zt
    y= -b - math.sqrt(b ** 2 - 4 * zt * c) / 2 * zt
    print('两个实数根为：',x,y)
except:
    print('无解')
