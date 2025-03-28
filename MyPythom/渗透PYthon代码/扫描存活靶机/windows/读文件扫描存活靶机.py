# -*- coding = utf-8 -*-
# @Time:2022/6/19 上午 文件检查文件:54
# @Author:CK
# @File:读文件扫描存活靶机
# @Software:PyCharm
import os
data = []
a_file = input("请输入文件名：")
a=open(a_file,'r')
b = a.readline().strip("\n")
while b!='':
    wang=os.popen('ping -n 1 -w 1 '+str(b)).readlines()
    ze=str(wang).find("TTL")
    if ze>=0:
        data.append(str(b))
    else:
        print(b,"\n login down")
    b = a.readline()
a.close()
print("----------------------------------------------------------------------")
if len(data) !=0:
    for i in data:
        print(i,end="")
else:
    print("检测范围内没有存活靶机")