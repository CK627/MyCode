# -*- coding = utf-8 -*-
# @Time:2021/11/30 10:41
# @Author: CK
# @File: 根据身份证判断出生日期.py
# @Software:PyCharm
import time
while True:
    try:
        ls = ['猴','鸡','狗','猪','鼠','牛','虎','兔','龙','蛇','马','羊']
        id=input('请输入你的身份证,按0后换行，退出并停止运行：')
        if id=='0':
            print('运行已终止')
            break
        if len(id)!=18 or not int(id[0:6]) or not int(id[14:17]):
            print('身份证格式错误，请从新输入')
            pass
        else:
            print('你出生于：',int(id[6:10]),'年',int(id[10:12]),'月',int(id[12:14]),'号')
            print('您的生日是：',int(id[10:12]),'月',int(id[12:14]),'号')
            age = int(time.strftime('%Y')) - int(id[6:10])
            sx = ls[-(14 - age % 12)]
            print('今年您：',age,'岁')
            print('属：',sx)
    except:
        print('身份证格式错误，请从新输入')