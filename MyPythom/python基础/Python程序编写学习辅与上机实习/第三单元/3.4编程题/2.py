# -*- coding = utf-8 -*-
# @Time:2022/6/23 下午 8:10
# @Author:CK
# @File:2
# @Software:PyCharm
'''
假设某国网民已有4.85亿，若每年以6.1%的速度增长，求多少年后，该国民将达到或超过8亿。变量建议：多少年为year，增长率为rate，网民数为s。程序运行结果如下。
9年后网名将有8.26380753218279亿，达到或超过8亿
'''
year=0
rate=0.061
s=4.85
while True:
    year=year+1
    s=s+s*rate
    if s>8:
        break

print('%s年后网名将有%s亿，达到或超过8亿'%(year,s))