# -*- coding = utf-8 -*-
# @Time: 2021/12/2720:09
# @Author： CK
# @File: 判断还有多少天过年
# @Software: PyCharm
year = int(input("请输入年:"))
month = int(input("请输入月:"))
day = int(input("请输入日:"))
months1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
months2 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
if 0 < month < 13 and 0 < day <= 31:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 100 == 0) and (year % 400 == 0):
        date = months1[month - 1] + day
        zt = 366 - date
    else:
        date = months2[month - 1] + day
        zt = 365 - date
    print("这一天是这一年的第%d天" % date)
    print('今年还剩%d天' % zt)
else:
    print('格式错误')
