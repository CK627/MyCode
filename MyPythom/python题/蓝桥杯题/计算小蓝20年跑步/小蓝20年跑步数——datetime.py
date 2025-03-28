# -*- codeing = utf-8 -*-
# @Time: 2021/12/1514:02
# @Author： CK
# @File: 蓝桥杯省赛
# @Ssftware: PyCharm
import datetime

rolling_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 10, 1)
days = datetime.timedelta(days=1)
count = 0

while(rolling_date <= end_date):
    if(rolling_date.day == 1 or rolling_date.isoweekday()==1):
        count += 2
    else:
        count += 1
    rolling_date += days

print(count)