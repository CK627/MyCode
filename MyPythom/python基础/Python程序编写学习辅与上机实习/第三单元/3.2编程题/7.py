'''
输入整数x、y、z，若x**2+y**2+z**2大于1000，则输出x**2+y**2+z**2的值；否则输出x、y、z三数之和。
'''
x=int(input('请输入整数x：'))
y=int(input('请输入整数y：'))
z=int(input('请输入整数z：'))
if x**2+y**2+z**2>1000:
    print(x**2+y**2+z**2)
else:
    print(x+y+z)