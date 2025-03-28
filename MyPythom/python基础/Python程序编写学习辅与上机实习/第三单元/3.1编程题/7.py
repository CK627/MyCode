'''
已知一个等差数列的前两项a1、a2，求第n项。a1、a2和n均由键盘输入。
'''
zt=int(input('请输入第一个正数：'))
b=int(input('请输入第二个正数：'))
c=int(input('请输入项数：'))
print(zt + (c - 1) * (b - zt))
