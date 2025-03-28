# -*- coding = utf-8 -*-
# @Time:2022/文件检查文件/27 下午 8:04
# @Author:CK
# @File:5
# @Software:PyCharm

import random
yzm=random.randint(99999,999999)
print("",yzm)
userpass=open('userpass.txt', 'r')
b = userpass.readline().strip()
zhtq=b[0:b.rfind(',')]
mmtq=b[b.rfind(","):].replace(",","")
while b!='':
    b = userpass.readline().strip()
userpass.close()

yzmsr=int(input("请输入验证码："))
if yzmsr==yzm:
    zh = input("请输入你的账号：")
    if zh==zhtq:
        mm = input("请输入你的密码：")
        if mm==mmtq:
            print("身份验证通过，欢迎登录")
        else:
            print("密码错误")
    else:
        print("账号错误")
else:
    print("验证码错误")