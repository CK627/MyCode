# -*- coding = utf-8 -*-
# @Time:2022/6/19 上午 文件检查文件:53
# @Author:CK
# @File:扫网段
# @Software:PyCharm
import os
data = []
for i in range(228,229):
    for x in range(1,255):
        wang=os.popen("ping -n 1 -w 1 10.194."+str(i)+"."+str(x)).readlines()
        ze=str(wang).find("TTL")
        if ze>=0:
            data.append("10.194."+str(i)+"."+str(x))
        else:
            print("10.194."+str(i)+"."+str(x)+"\n login down")

print("----------------------------------------------------------------------")
if len(data) !=0:
    for i in data:
        print(i)
else:
    print("检测范围内没有存活靶机")
