'''
计算两点距离。输入两点坐标（x1,y1）,(x2,y2)，计算并输出两点间的距离。
'''
import math
x1,y1=input('请输入点x1和y1中间用英文的逗号隔开:').split(',')
x2,y2=input('请输入点x2和y2中间用英文的逗号隔开:').split(',')
print('两点距离为：',abs(math.sqrt((int(x1)-int(x2))**2)-(int(y1)-int(y2))**2))