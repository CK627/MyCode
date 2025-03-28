"""
从键盘输入年份和月份，输出它处于什么季节，当月有几天。
"""
import time
rennian=[31,29,31,30,31,30,31,31,30,31,30,31]
pingnian=[31,28,31,30,31,30,31,31,30,31,30,31]
zt, b=input('请输入它的年份和月份,用空格隔开：').split(' ')
zt, b= int(zt), int(b)
if zt%4==0 or zt%400==0:
    if 1<=b<=3:
        print('春季','当月有'+str(rennian[b-1])+'天')
    elif 4<=b<=6:
        print('夏季','当月有'+str(rennian[b-1])+'天')
    elif 7<=b<=9:
        print('秋季','当月有'+str(rennian[b-1])+'天')
    else:
        print('冬季','当月有'+str(rennian[b-1])+'天')
else:
    if 1<=b<=3:
        print('春季','当月有'+str(pingnian[b-1])+'天')
    elif 4<=b<=6:
        print('夏季','当月有'+str(pingnian[b-1])+'天')
    elif 7<=b<=9:
        print('秋季','当月有'+str(pingnian[b-1])+'天')
    else:
        print('冬季','当月有'+str(pingnian[b-1])+'天')