'''
判断输入的正整数是否既是5又是7的整倍数。若是，则输出yes；否则输出no。
'''
zt=int(input('请输入一个整数：'))
if zt%5==0 and zt%7==0:
    print('yes')
else:
    print('no')