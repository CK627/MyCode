# -*- coding = utf-8 -*-
# @Time: 2021/12/3011:13
# @Author： CK
# @File: 判断数字所在的位数
# @Software: PyCharm
try:
    zt=int(input('请输入一个三位数的整数：'))
    Hundredth = zt // 100  # 求百位数
    Ten = (zt // 10) % 10  # 求十位数
    Bit = (zt % 100) % 10  # 求个位数
    print('百位是：',Hundredth)
    print('十位是：',Ten)
    print('个位是：',Bit)
except:
    print('格式错误，请重新输入。')