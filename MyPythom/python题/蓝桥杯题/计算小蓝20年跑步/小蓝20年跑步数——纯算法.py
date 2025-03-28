# -*- codeing = utf-8 -*-
# @Time: 2021/11/3015:16
# @Author： CK
# @File: 小蓝20年跑步数.py
# @Ssftware: PyCharm
'''
小蓝每天都锻炼身体。
正常情况下，小蓝每天跑1千米。如果某天是周一或者月初（1日），为了激励自己，小蓝要跑2千米。如果同时是周一或月初，小蓝也是跑2千米。
小蓝跑步已经坚持了很长时间，从2000年1月1日周六（含）到2020年10月1日周四（含）。请问这段时间小蓝总共跑步多少千米？
'''
year = 2000 # 设置变量并赋值2000，在这里意思是年
month = 1 # 设置变量并赋值1，在这里意思是月
data_index = 1 # 设置变量并赋值1，在这里意思是数据索引，初始值为1，用来储存临时数据
week_index = 6 # 设置变量并赋值6，在这里意思是星期
flags = []  # 创建一个空列表，用于存放每天跑步的公里数

while (year != 2020) or (month != 10) or (data_index != 2): # 条件循环，中间用or连接，意思是当中有一个条件完成就停止循环
    if week_index == 1 or data_index == 1: # 判断是否为星期一或月初
        flags.append(2) # 是就在列表末尾加2
    else: # 否则
        flags.append(1) # 不是就在列表末尾加1

    if month == 4 or month == 6 or month == 9 or month == 11: # 判断月份是大月还是小月
        if not (data_index % 30): # 判断deta_index能不能整除30
            month += 1 # 能就加1
        data_index = data_index % 30 + 1 # 回归初始值
    elif month == 2: # 利用二月来区分闰年
        if (not (year % 4) and (year % 100)) or not (year % 400): # 判断是否为闰年
            if not (data_index % 29): # 判断deta_index能不能整除29
                month += 1 # 能就加1
            data_index = data_index % 29 + 1 # 回归初始值
        else: # 否则
            if not (data_index % 28): # 判断deta_index能不能整除28
                month += 1 # 能就加1
            data_index = data_index % 28 + 1 # 回归初始值
    else: # 否则
        if month == 12: # 判断月份是否到了12月
            if not (data_index % 31): # 判断deta_index能不能整除31
                month = month % 12 + 1 # 回归初始值
                year += 1  # 新的一年
        else: # 否则
            if not (data_index % 31): # 判断deta_index能不能整除31
                month += 1 # 能就加1
        data_index = data_index % 31 + 1 # 回归初始值

    week_index = week_index % 7 + 1 # 回归初始值，将星期调回星期一

print(sum(flags))#sum:python内置函数，用于将所有的值想加