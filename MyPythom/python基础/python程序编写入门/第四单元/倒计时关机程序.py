# -*- coding = utf-8 -*-
# @Time: 2022/1/615:48
# @Author： CK
# @File: 倒计时关机程序
# @Software: PyCharm
import time
zt=int(input('请输入倒计时秒数：'))
b=zt
print('倒计时开始：')
for i in range(zt):
    print('还剩%d秒'%b)
    time.sleep(1)
    b=b-1
    c=b
    if c<=4:
        for d in range(1,c):
            print('还剩%d秒'%c)
            print('警告，马上关机！')
            time.sleep(1)
            c=c-1
    if c<=1:
        print('还剩%d秒'%c)
        print('***时间到了！开始关机***')
        break