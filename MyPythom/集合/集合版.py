# -*- coding = utf-8 -*-
# @Time:2023/2/15 18:46
# @Author:CK
# @File:集合版
# @Software:PyCharm

from PIL import Image
from plyer import notification
from pystray import *
import threading, psutil, os, sys, pystray, time, re, datetime, socket, smtplib
from pystray import Icon as icon, Menu as menu, MenuItem as item

import PySimpleGUI as sg
import tkinter as tk
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText


class Batch_remove_and_add_suffix:
    def __init__(self):
        self.__list1 = []

    def print_files(self, path):
        lsdir = os.listdir(path)
        dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
        files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
        if files:
            for f in files:
                self.__list1.append(os.path.join(path, f).replace("\\", r'/'))
        if dirs:
            for d in dirs:
                Batch_remove_and_add_suffix().print_files(os.path.join(path, d))

    def tianjia(self, filedir, suffix):
        files = os.listdir(filedir)
        for filename in files:
            portion = os.path.splitext(filename)
            filename = filedir + '\\' + filename  # 路劲与文件名整合全量
            if os.path.isfile(filename):  # 判断在输入的路径下，是文件还是文件夹
                if portion[1] != suffix:
                    os.rename(filename, filedir + '\\' + portion[0] + portion[1] + suffix)

    def tianjia2(self, filedir, suffix):
        for root, dirs, files in os.walk(filedir):
            for file in files:
                Batch_remove_and_add_suffix().tianjia(filedir, suffix)
            for dir1 in dirs:
                NewDir = os.path.join(root, dir1)
                Batch_remove_and_add_suffix().tianjia(NewDir, suffix)

    def quchu(self, filedir, suffix):
        files = os.listdir(filedir)
        for filename in files:
            portion = os.path.splitext(filename)
            filename = filedir + '\\' + filename  # 路劲与文件名整合全量
            if os.path.isfile(filename):  # 判断在输入的路径下，是文件还是文件夹
                if portion[1] == suffix:
                    os.rename(filename, filedir + '\\' + portion[0])

    def quchu2(self, filedir, suffix):
        for root, dirs, files in os.walk(filedir):
            for file in files:
                Batch_remove_and_add_suffix().quchu(filedir, suffix)
            for dir in dirs:
                NewDir = os.path.join(root, dir)
                Batch_remove_and_add_suffix().quchu(NewDir, suffix)

    def GUI(self, icon: pystray.Icon, item):
        layout = [
            [sg.Text("后缀名添加与删除", grab=True)],
            [sg.Text("使用说明：\n点击“文件路径”可以弹出资源管理器选择文件夹\n鼠标悬浮在输入框有提示")],
            [sg.Text("文件路径", enable_events=True, tooltip=f'输入或者选择文件路径', size=(15, 1)),
             sg.In("", key='file_path', enable_events=True, tooltip=f'实例：C:/Users/Administrator/Desktop')],
            [sg.Text("后缀名", enable_events=True, tooltip=f'输入要转换的文件后缀名', size=(15, 1)),
             sg.In("", key='Suffix_name', tooltip=f'示例：.txt')],
            [sg.B("增加"), sg.B("删除"), sg.B("退出")],
        ]

        sg.theme("LightBlue2")
        window = sg.Window("后缀名添加与删除", layout)
        icon.notify("已开启后缀名添加与删除")

        while True:
            event, values = window.read()
            if event is None:
                break
            if event == "增加":
                Batch_remove_and_add_suffix().tianjia2(values["file_path"], values["Suffix_name"])
                icon.notify("增加成功")
            if event == "删除":
                Batch_remove_and_add_suffix().quchu2(values["file_path"], values["Suffix_name"])
                icon.notify("删除成功")
            if event == "退出":
                icon.notify("已关闭后缀名添加与删除")
                break
            if event == "文件路径":
                root = tk.Tk()
                root.withdraw()
                File = filedialog.askdirectory()
                window["file_path"].update(File)
        window.close()


class Monitoring_IP(threading.Thread):  # 检测WiFi的改变
    jsq = 0

    def __init__(self, *args, **kwargs):
        super(Monitoring_IP, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def gei_IP_socket(self=None):  # 获取WiFi的IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        IP_gei = s.getsockname()[0]
        return IP_gei

    def Mail_send(self=None):  # 有网发送邮件
        with open("日志.txt", "a+", encoding="utf-8") as wdwfs:
            try:
                con = smtplib.SMTP_SSL("smtp.qq.com", 465)
                con.login("3340324320@qq.com", "rszmqgxdxapacjed")
                msg = MIMEMultipart()
                msg["Subject"] = Header("更改的IP地址", "utf-8").encode()
                msg["From"] = "3340324320@qq.com <3340324320@qq.com>"
                msg["To"] = "3340324320@qq.com"
                sj = str(datetime.datetime.now())
                text = MIMEText(sj + ':     ' + self.ipconfig + "-----------更新后-----------" + self.ipconfig2,
                                "plain", "utf-8")
                msg.attach(text)
                con.sendmail('3340324320@qq.com', "3340324320@qq.com", msg.as_string())
                w = str(datetime.datetime.now())
                wdwfs.write(w + ":    " + "邮件发送成功" + "\n")
                icon.notify("邮件发送成功")
                con.quit()
                jsq = self.jsq + 1
            except:
                if self.ze >= 0:
                    w = str(datetime.datetime.now())
                    wdwfs.write(w + ":    " + "邮件发送失败，请检查你的邮箱是否填写正确。" + "\n")
                    icon.notify("邮件发送失败，请检查你的邮箱是否填写正确。")
                else:
                    w = str(datetime.datetime.now())
                    wdwfs.write(w + ":    " + "邮件发送失败，请检查你的网络。" + '\n')
                    icon.notify("邮件发送失败，请检查你的网络。")
            wdwfs.close()

    def dwfsOffline_mail(self=None):  # 断网后恢复网络发送邮件
        with open("日志.txt", "a+", encoding="utf-8") as dwfs:
            try:
                con = smtplib.SMTP_SSL('smtp.qq.com', 465)
                con.login("3340324320@qq.com", "rszmqgxdxapacjed")
                msg = MIMEMultipart()
                msg["Subject"] = Header("网络异常时间段的IP改变", 'utf-8').encode()
                msg["From"] = "3340324320@qq.com <3340324320@qq.com>"
                msg['To'] = '3340324320@qq.com'
                file1 = open("断网IP.txt", "rb").read()
                text = MIMEText(str(file1), "base64", "utf-8")
                text["Content-Disposition"] = 'attachment; filename = "ip.txt"'
                msg.attach(text)
                con.sendmail("3340324320@qq.com", "3340324320@qq.com", msg.as_string())
                con.quit()
                w = str(datetime.datetime.now())
                dwfs.write(w + ":    " + "邮件发送成功_断网" + '\n')
                icon.notify("邮件发送成功_断网")
            except:
                zcjc = os.popen("ping -n 1 -w 1000 " + "www.baidu.com").readlines()
                zcjc_a = str(zcjc).find("TTL")
                if zcjc_a >= 0:
                    w = str(datetime.datetime.now())
                    dwfs.write(w + ":    " + "邮件发送失败_断网，请检查你的邮箱是否填写正确。" + "\n")
                    icon.notify("邮件发送失败_断网，请检查你的邮箱是否填写正确。")
                w = str(datetime.datetime.now())
                dwfs.write(w + ":    " + "邮件发送失败_断网，请检查你的邮箱是否填写正确。" + '\n')
                icon.notify("邮件发送失败_断网，请检查你的邮箱是否填写正确。")
            dwfs.close()

    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            with open("日志.txt", "a+", encoding="utf-8") as a:
                self.ipconfig = Monitoring_IP.gei_IP_socket()
                time.sleep(0.5)
                self.ipconfig2 = Monitoring_IP.gei_IP_socket()
                ip = re.search(self.ipconfig2, self.ipconfig)
                t = str(datetime.datetime.now())
                a.write(t + ":    " + str(ip) + '\n')
                wang = os.popen("ping -n 1 -w 1000 " + "www.baidu.com").readlines()
                self.ze = str(wang).find("TTL")
                Memory = round(os.path.getsize("日志.txt") / 1024 / 1024)
                if Memory >= 50:
                    os.unlink("日志.txt")
                    icon.notify("日志删除")
                else:
                    pass
                try:
                    if ip is None and self.ze >= 0:
                        Monitoring_IP.Mail_send()
                        pass
                    elif ip is None and self.ze <= 0:
                        continue
                    elif self.ze >= 0 and self.jsq < 1 and ip is None:
                        Monitoring_IP.dwfsOffline_mail()
                        os.unlink("断网IP.txt")
                        pass

                    elif ip is None and self.ze <= 0:
                        with open("断网IP.txt", "a+") as b:
                            c = str(datetime.datetime.now())
                            b.write(
                                c + ':      ' + self.ipconfig + "-----------更新后-----------" + self.ipconfig2 + '\n')
                            c1 = str(datetime.datetime.now())
                            a.write(c1 + ":     " + "已经加入文件" + '\n')
                            icon.notify("已经加入文件")
                            continue
                    else:
                        continue
                except:
                    continue
                self.jsq = 0

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()


m = Monitoring_IP()
m.daemon = True

run_start_Monitoring_IP_state = False
run_pause_Monitoring_IP_state = False
run_resume_Monitoring_IP_state = False
run_stop_Monitoring_IP_state = False
start_Monitoring_IP_a_and_b = True
stop_Monitoring_IP_a_and_b = False
resume_Monitoring_IP_a_and_b = False
pause_Monitoring_IP_a_and_b = False


def run_start_Monitoring_IP(icon: pystray.Icon, item, ):
    global run_start_Monitoring_IP_state
    global stop_Monitoring_IP_a_and_b
    global run_resume_Monitoring_IP_state
    global pause_Monitoring_IP_a_and_b
    global start_Monitoring_IP_a_and_b
    start_Monitoring_IP_a_and_b = False
    pause_Monitoring_IP_a_and_b = True
    stop_Monitoring_IP_a_and_b = True
    run_resume_Monitoring_IP_state = True
    run_start_Monitoring_IP_state = not item.checked
    m.start()
    if m.is_alive():
        icon.notify("检测WiFi的改变功能已启动")


def run_pause_Monitoring_IP(icon: pystray.Icon, item, ):
    global run_pause_Monitoring_IP_state
    global run_resume_Monitoring_IP_state
    global run_start_Monitoring_IP_state
    global start_Monitoring_IP_a_and_b
    global stop_Monitoring_IP_a_and_b
    global resume_Monitoring_IP_a_and_b
    start_Monitoring_IP_a_and_b = False
    run_start_Monitoring_IP_state = False
    resume_Monitoring_IP_a_and_b = True
    stop_Monitoring_IP_a_and_b = True
    run_pause_Monitoring_IP_state = not item.checked
    run_resume_Monitoring_IP_state = False
    m.pause()
    if m.is_alive():
        icon.notify("检测WiFi的改变功能已暂停")


def run_resume_Monitoring_IP(self: pystray.Icon, item, ):
    global run_resume_Monitoring_IP_state
    global run_start_Monitoring_IP_state
    global run_pause_Monitoring_IP_state
    global start_Monitoring_IP_a_and_b
    global resume_Monitoring_IP_a_and_b
    resume_Monitoring_IP_a_and_b = False
    start_Monitoring_IP_a_and_b = False
    run_pause_Monitoring_IP_state = False
    run_resume_Monitoring_IP_state = not item.checked
    run_start_Monitoring_IP_state = True
    m.resume()
    if m.is_alive():
        self.notify("检测WiFi的改变功能继续执行")



def run_stop_Monitoring_IP(icon: pystray.Icon, item, ):
    global run_stop_Monitoring_IP_state
    global run_start_Monitoring_IP_state
    global run_resume_Monitoring_IP_state
    global run_pause_Monitoring_IP_state
    global stop_Monitoring_IP_a_and_b
    global pause_Monitoring_IP_a_and_b
    global start_Monitoring_IP_a_and_b
    global resume_Monitoring_IP_a_and_b
    resume_Monitoring_IP_a_and_b = False
    start_Monitoring_IP_a_and_b = False
    pause_Monitoring_IP_a_and_b = False
    stop_Monitoring_IP_a_and_b = False
    run_pause_Monitoring_IP_state = False
    run_resume_Monitoring_IP_state = False
    run_start_Monitoring_IP_state = False
    run_stop_Monitoring_IP_state = not item.checked
    m.stop()
    if not m.is_alive():
        icon.notify("检测WiFi的改变功能已停止\n脚本关闭意味着线程关闭，请重启后开启脚本！！！")


class kill_kali_linux(threading.Thread):  # 检测后台进程存活

    def __init__(self, *args, **kwargs):
        super(kill_kali_linux, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def run(self, *process_name):
        while self.__running.is_set():
            self.__flag.wait()
            for proc in psutil.process_iter():
                if proc.name() == process_name:
                    os.system(f'taskkill /IM {process_name} /F')
                    # icon.notify("已检测到进程“vmmem”存在自动kill中")
                    notification.notify(title="Python通知",
                                        message=f"已检测到进程{process_name}存在\n自动自动结束进程中", timeout=3)

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()

    def GUI(self, icon: pystray.Icon, item):
        layout = [
            [sg.Text("进程检测系统", grab=True)],
            [sg.Text("使用说明：\n点击“文件路径”可以弹出资源管理器选择文件夹\n鼠标悬浮在输入框有提示")],
            [sg.Text("文件路径", enable_events=True, tooltip=f'输入或者选择文件路径', size=(15, 1)),
             sg.In("", key='file_path', enable_events=True, tooltip=f'实例：C:/Users/Administrator/Desktop')],
            [sg.B("增加"), sg.B("删除"), sg.B("退出")],
        ]

        sg.theme("LightBlue2")
        window = sg.Window("后缀名添加与删除", layout)
        icon.notify("已开启后缀名添加与删除")

        while True:
            event, values = window.read()
            if event is None:
                break
            if event == "增加":
                Batch_remove_and_add_suffix().tianjia2(values["file_path"], values["Suffix_name"])
                icon.notify("增加成功")
            if event == "删除":
                Batch_remove_and_add_suffix().quchu2(values["file_path"], values["Suffix_name"])
                icon.notify("删除成功")
            if event == "退出":
                icon.notify("已关闭后缀名添加与删除")
                break
            if event == "文件路径":
                root = tk.Tk()
                root.withdraw()
                File = filedialog.askdirectory()
                window["file_path"].update(File)
        window.close()


a = kill_kali_linux()
a.daemon = True

run_start_kali_linux_state = False
run_pause_kali_linux_state = False
run_resume_kali_linux_state = False
run_stop_kali_linux_state = False
start_kali_linux_a_and_b = True
stop_kali_linux_a_and_b = False
resume_kali_linux_a_and_b = False
pause_kali_linux_a_and_b = False


def run_start_kali_linux(icon: pystray.Icon, item, ):
    global run_start_kali_linux_state
    global stop_kali_linux_a_and_b
    global run_resume_kali_linux_state
    global pause_kali_linux_a_and_b
    global start_kali_linux_a_and_b
    start_kali_linux_a_and_b = False
    pause_kali_linux_a_and_b = True
    stop_kali_linux_a_and_b = True
    run_resume_kali_linux_state = True
    run_start_kali_linux_state = not item.checked
    a.start()
    if a.is_alive():
        icon.notify(f"检测进程存活功能已启动")


def run_pause_kali_linux(icon: pystray.Icon, item, ):
    global run_pause_kali_linux_state
    global run_resume_kali_linux_state
    global run_start_kali_linux_state
    global start_kali_linux_a_and_b
    global stop_kali_linux_a_and_b
    global resume_kali_linux_a_and_b
    start_kali_linux_a_and_b = False
    run_start_kali_linux_state = False
    resume_kali_linux_a_and_b = True
    stop_kali_linux_a_and_b = True
    run_pause_kali_linux_state = not item.checked
    run_resume_kali_linux_state = False
    a.pause()
    if a.is_alive():
        icon.notify("检测进程存活功能已暂停")


def run_resume_kali_linux(self: pystray.Icon, item, ):
    global run_resume_kali_linux_state
    global run_start_kali_linux_state
    global run_pause_kali_linux_state
    global start_kali_linux_a_and_b
    global resume_kali_linux_a_and_b
    resume_kali_linux_a_and_b = False
    start_kali_linux_a_and_b = False
    run_pause_kali_linux_state = False
    run_resume_kali_linux_state = not item.checked
    run_start_kali_linux_state = True
    a.resume()
    if a.is_alive():
        self.notify("检测进程存活功能继续执行")


def run_stop_kali_linux(icon: pystray.Icon, item, ):
    global run_stop_kali_linux_state
    global run_start_kali_linux_state
    global run_resume_kali_linux_state
    global run_pause_kali_linux_state
    global stop_kali_linux_a_and_b
    global pause_kali_linux_a_and_b
    global start_kali_linux_a_and_b
    global resume_kali_linux_a_and_b
    resume_kali_linux_a_and_b = False
    start_kali_linux_a_and_b = False
    pause_kali_linux_a_and_b = False
    stop_kali_linux_a_and_b = False
    run_pause_kali_linux_state = False
    run_resume_kali_linux_state = False
    run_start_kali_linux_state = False
    run_stop_kali_linux_state = not item.checked
    a.stop()
    if not a.is_alive():
        icon.notify("检测进程存活功能已停止\n脚本关闭意味着线程关闭，请重启后开启脚本！！！")
    # a = kill_kali_linux()
    # a.daemon = True


def restart(icon: pystray.Icon, item, ):
    icon.notify("重启脚本\n脚本已重启")
    time.sleep(0.5)
    python = sys.executable
    os.execl(python, python, *sys.argv)


def on_exit(icon: pystray.Icon, item):
    icon.notify("关闭脚本\n脚本已关闭")
    time.sleep(0.5)
    icon.stop()


image = Image.open('1.jpg')
icon('test', image, menu=menu(
    item('检测进程存活功能',
         menu(
             MenuItem(text='添加要检测的进程', action=kill_kali_linux().GUI),
             MenuItem(text='检测进程存活功能启动', action=run_start_kali_linux,
                      checked=lambda item: run_start_kali_linux_state, enabled=lambda item: start_kali_linux_a_and_b),
             MenuItem(text='检测进程存活功能暂停', action=run_pause_kali_linux,
                      checked=lambda item: run_pause_kali_linux_state, enabled=lambda item: pause_kali_linux_a_and_b),
             MenuItem(text='检测进程存活功能继续执行', action=run_resume_kali_linux,
                      checked=lambda item: run_resume_kali_linux_state, enabled=lambda item: resume_kali_linux_a_and_b),
             MenuItem(text='检测进程存活功能停止', action=run_stop_kali_linux,
                      checked=lambda item: run_stop_kali_linux_state, enabled=lambda item: stop_kali_linux_a_and_b),
         )
         ),
    item('检测WiFi的改变功能',
         menu(
             MenuItem(text='检测WiFi的改变功能启动', action=run_start_Monitoring_IP,
                      checked=lambda item: run_start_Monitoring_IP_state,
                      enabled=lambda item: start_Monitoring_IP_a_and_b),
             MenuItem(text='检测WiFi的改变功能暂停', action=run_pause_Monitoring_IP,
                      checked=lambda item: run_pause_Monitoring_IP_state,
                      enabled=lambda item: pause_Monitoring_IP_a_and_b),
             MenuItem(text='检测WiFi的改变功能继续执行', action=run_resume_Monitoring_IP,
                      checked=lambda item: run_resume_Monitoring_IP_state,
                      enabled=lambda item: resume_Monitoring_IP_a_and_b),
             MenuItem(text='检测WiFi的改变功能停止', action=run_stop_Monitoring_IP,
                      checked=lambda item: run_stop_Monitoring_IP_state,
                      enabled=lambda item: stop_Monitoring_IP_a_and_b),
         )
         ),
    item("增加或删除文件名后缀",
         menu(
             MenuItem(text='增加或删除文件名后缀功能开启', action=Batch_remove_and_add_suffix().GUI),
         )
         ),
    item("程序列表",
         menu(
             MenuItem(text='重启脚本', action=restart),
             MenuItem(text='退出脚本', action=on_exit),
         )
         ),
    MenuItem(text='Python检测进程存活启动', action=run_start_kali_linux, default=True, visible=False,
             checked=lambda item: run_start_kali_linux_state)
)
     ).run()
