# -*- coding = utf-8 -*-
# @Time:2021/11/30 10:33
# @Author: CK
# @File: 话费充值.py
# @Software:PyCharm
# 这里用中文作变量名是为了更好理解，但在一般情况下最好还是用英文来用作变量名
q=input('是否查看自己的话费余额？(Y/N):')
if q== 'Y':
    a=input('当前用户话费余额还剩8元，是否充值？(Y/N)')
    if a== 'Y':
        for jh in range(1, 6):
            mm=input('请输入您的密码：')
            if mm== '1':
                b=int(input('请输入想充值的金额：'))
                # 充值的金额= 充值的金额 + 8
                print('恭喜您，充值成功！当前话费余额还有', b + 8, '元')
                break
            elif jh<5:
                    print('对不起，您输入的密码有误，您还有', 5 - jh, '次重试机会')
        else:
            print('对不起，操作失败')
    elif a== 'N':
         print('您已取消充值')
else:
    print('您已取消')
