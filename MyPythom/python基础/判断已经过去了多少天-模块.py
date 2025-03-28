# -*- coding = utf-8 -*-
# @Time: 2021/12/2811:14
# @Author： CK
# @File: 判断已经过去了多少天-模块
# @Software: PyCharm
import datetime
year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入当月哪一天:"))
targetDay = datetime.date(year, month, day)
dayCount = targetDay - datetime.date(targetDay.year - 1 ,12, 31)
print("%s是%s年的第%s天." %(targetDay, targetDay.year, dayCount))