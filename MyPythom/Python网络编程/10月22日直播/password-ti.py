"""
本题以 mysql弱口令为例
pip install pymysql
"""

import pymysql

# 目标ip
target_ip = '127.0.0.1'
# 读取弱口令文件
# 本机测试读取文件首会有诡异的\ufeff  用 encoding='utf-8-sig'即可解决
fp = open('6000常用密码字典加强版.txt', 'r', encoding='utf-8-sig')
# 去掉空格
pwd_list = [__F1__]
# 关闭文件连接
fp.close()
result_pwd = ''
for i in pwd_list:
    # 使用 pymysql连接 mysql
    # 如果密码错误则会抛出异常
    try:
        db = pymysql.connect(
            host=__F2__,
            port=3306,
            user="root",
            password=__F3__,
            connect_timeout=2)
    except:
        # 连接失败
        __F4__
    # 密码只有一个，连接成功就可以直接结束了
    result_pwd = i
    __F5__

# 判断result的值即可知道是否爆破成功
if __F6__:
    print(f"{target_ip}连接成功，密码为：{result_pwd}")
else:
    print('爆破失败')
