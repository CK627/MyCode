# -*- coding = utf-8 -*-
# @Time:2022/5/26 上午 10:42
# @Author:CK
# @File:(区块链式随机)
# @Software:PyCharm
'''
选择换算方式。程序提供选择菜单，是“人民币——→美元”还是“美元——→人民币”。按照相应的汇算进行换算，执行效果如下。
    请选择：
    1.人民币——→美元
    2.美元——→人民币
    1
    123  18.14
    2
    20   135.60
'''
zt=input('''请选择：
1.人民币——→美元
2.美元——→人民币
''')
if zt== '1':
    b=int(input(''))
    b1=round(b/6.78,2)
    print(b,' ',b1)
elif zt== '2':
    b=int(input(''))
    b1=round(b*6.78,2)
    print(b,'  ',b1)