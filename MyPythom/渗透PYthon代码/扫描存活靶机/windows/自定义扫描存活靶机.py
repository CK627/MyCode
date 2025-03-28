# -*- coding = utf-8 -*-
# @Time:2022/6/19 上午 文件检查文件:55
# @Author:CK
# @File:自定义扫描存活靶机
# @Software:PyCharm
import os
data = []
a,b,c,d=input("输入开始ip：").split(".")
q,w,e,r=input("输入结束ip：").split(".")
for i in range(int(a),int(q)+1):
    for x in range(int(b),int(w)+1):
        for l in range(int(c),int(e)+1):
            for y in range(int(d),int(r)+1):
                wang=os.popen("ping -n 1 -w 1 "+str(i)+"."+str(x)+"."+str(l)+"."+str(y)).readlines()
                ze=str(wang).find("TTL")
                if ze>=0:
                    data.append(str(i)+"."+str(x)+"."+str(l)+"."+str(y))
                else:
                    print(str(i)+"."+str(x)+"."+str(l)+"."+str(y)+"\n login down")

print("----------------------------------------------------------------------")
if len(data) !=0:
    for i in data:
        print(i)
else:
    print("检测范围内没有存活靶机")
