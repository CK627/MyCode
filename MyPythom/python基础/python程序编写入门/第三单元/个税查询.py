# -*- coding = utf-8 -*-
# @Time: 2021/12/2317:55
# @Author： CK
# @File: 个税查询
# @Software: PyCharm
pay = int(input('请输入本年收入：'))
grade = 0
pay2 = pay-60000
if pay2 < 0:
    tax = 0
elif pay2 < 36000:
    tax = pay2 * 0.03 - 0
    grade = 1
elif 36000 <= pay2 < 144000:
    tax = pay2 * 0.1 - 2520
    grade=2
elif 144000 <= pay2 < 300000:
    tax = pay2 * 0.2 - 16920
    grade=3
elif 300000 <= pay2 < 420000:
    tax = pay2 * 0.25 - 31920
    grade=4
elif 420000 <= pay2 < 660000:
    tax = pay2 * 0.3 - 52920
    grade=5
elif 660000 <= pay2 < 960000:
    tax = pay2 * 0.35 - 85920
    grade=6
else:
    tax = pay2 * 0.45 - 181920
    grade=7
print('您的应纳个人所得税税额是：', tax,"所对应的级数为：",grade,"级")