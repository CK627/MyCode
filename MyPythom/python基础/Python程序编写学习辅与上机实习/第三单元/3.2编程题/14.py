'''
由键盘输入3个整数a、b、c，输出其中最大的数。
'''
zt, b, c=input('请输入三个数，(用空格隔开)：').split(' ')
zt, b, c= int(zt), int(b), int(c)
if zt>b and zt>c:
    print(zt)
elif b>zt and b>c:
    print(b)
else:
    print(c)