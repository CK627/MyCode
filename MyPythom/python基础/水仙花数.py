# -*- coding = utf-8 -*-
# @Time: 2021/12/2713:09
# @Author： CK
# @File: 水仙花数
# @Software: PyCharm
try:
    name1 = int(input('请输入一个三位数的整数：'))
    while True :
        Hundredth=name1//100 #求百位数
        Ten=(name1//10)%10 #求十位数
        Bit=(name1%100)%10 #求个位数
        if Hundredth**3+Ten**3+Bit**3==name1:
            print(name1,'是水仙花数')
            break
        else:
            print(name1,'不是水仙花数')
            break
except:
    print('请重新运行并输入一个三位数的整数')