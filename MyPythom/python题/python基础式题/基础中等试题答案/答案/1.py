# -*- coding = utf-8 -*-
# @Time:2022/6/10 下午 文件检查文件:42
# @Author:CK
# @File:1
# @Software:PyCharm

# 使用库
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

# 纯算法

year = 2000
month = 1
data_index = 1
week_index = 6
flags = []

while (year != 2020) or (month != 10) or (data_index != 2):
    if week_index == 1 or data_index == 1:
        flags.append(2)
    else:
        flags.append(1)

    if month == 4 or month == 6 or month == 9 or month == 11:
        if not (data_index % 30):
            month += 1
        data_index = data_index % 30 + 1
    elif month == 2:
        if (not (year % 4) and (year % 100)) or not (year % 400):
            if not (data_index % 29):
                month += 1
            data_index = data_index % 29 + 1
        else:
            if not (data_index % 28):
                month += 1
            data_index = data_index % 28 + 1
    else:
        if month == 12:
            if not (data_index % 31):
                month = month % 12 + 1
                year += 1
        else:
            if not (data_index % 31):
                month += 1
        data_index = data_index % 31 + 1

    week_index = week_index % 7 + 1

print(sum(flags))
