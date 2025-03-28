'''
变换两个变量值。定义变量first和second，从键盘输入两个数分别存放于first和second中，输出这两个变量的值。然后，交换这两个变量的值，再输出这两个变量的值。
'''
first=input('请输入第一个数：')
second=input('请输入第二个数：')
print(first,second)
first,second=second,first
print(first,second)