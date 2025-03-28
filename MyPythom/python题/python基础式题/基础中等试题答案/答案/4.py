# -*- coding = utf-8 -*-
# @Time:2022/文件检查文件/22 上午 8:19
# @Author:CK
# @File:文件检查文件
# @Software:PyCharm
intCount = []
lowerCount = []
upperCount = []
otherCount = []
s = input("请输入一个字符串：")
for i in s:
    if i.isdigit():
        intCount.append(i)
    elif i.islower():
        lowerCount.append(i)
    elif i.isupper():
        upperCount.append(i)
    else:
        otherCount.append(i)

print('数字的个数：',"".join(intCount))
print('小写字母的个数：',"".join(lowerCount))
print('大写字母的个数：',"".join(upperCount))
print('其他字符的个数：',"".join(otherCount))