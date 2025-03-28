'''
                         {-1（x<0）
编写程序，输入x的值，根据函数y{0 （x=0）,输出y的值。
                         {1 （X>0）
'''
x=int(input('请输入x的值：'))
if x<0:
    print(-1)
elif x==0:
    print(0)
else:
    print(1)