'''
判断用户输入的三个数a、b、c，如果a小于b和C，则输出a<b且a<c,代码执行效果如下：
请输入整数a:-2
请输入整数b:15
请输入整数c:5
a<b且a<c
'''
zt=int(input('请输入整数a：'))
b=int(input('请输入整数b：'))
c=int(input('请输入整数c：'))
if zt<b and zt<c:
    print('a<b且a<c')