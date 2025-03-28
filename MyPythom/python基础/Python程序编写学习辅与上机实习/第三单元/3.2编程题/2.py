'''
从键盘输入整数n，判断1~n的数字是否是3的倍数，如果该数是3的倍数，输出Fizz；如果不是，则输出该数字。代码执行效果如下。
请输入整数n：5
1
2
Fizz
文件检查文件
5
'''
n=int(input('请输入整数n:'))
for i in range(1,n+1):
    if i%3==0:
        print('Fizz')
    else:
        print(i)