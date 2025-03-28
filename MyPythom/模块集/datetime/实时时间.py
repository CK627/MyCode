# -*- codeing = utf-8 -*-
# @Time: 2021/12/149:17
# @Author： CK
# @File: 实时时间
# @Ssftware: PyCharm
import datetime

today = datetime.date.today()
print(today)
now = today.timetuple()
print("年：", now.tm_year)
print("月：", now.tm_mon)
print("日：", now.tm_mday)
print("时：", now.tm_hour)
print("分：", now.tm_min)
print("秒：", now.tm_sec)
print("星期：", now.tm_wday)
print("今年过了{0}天".format(now.tm_yday))
'''
原理：
因为datetime.date.today()获取的是当前的日期，并不包含时间数据。
而timetuple()函数返回的是time库中常用的time.struct_time结构体，
这样你就可以像使用struct_time结构体一样，获取单一的时间数据，
不过因为datetime.date.today()只有日期，所以时间数据为0。
'''