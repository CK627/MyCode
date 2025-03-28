# -*- coding = utf-8 -*-
# @Time:2024/11/13 21:04
# @Author:ck
# @File:进程检测
# @Software:PyCharm

import psutil
import os
import time
import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image
from datetime import datetime

running = False
paused = False
process_list = ['WeChat', 'Notes']
log_file = 'log.txt'

def write_log(message):
    with open(log_file, 'a', encoding='utf-8') as file:
        file.write(f"{datetime.now()} - {message}\n")

def detect_and_kill_processes():
    global running, paused
    while running:
        if paused:
            time.sleep(1)
            continue
        for proc in psutil.process_iter(['pid', 'name', 'create_time']):
            try:
                proc_name = proc.info['name']
                if proc_name in process_list:
                    pid = proc.info['pid']
                    start_time = datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')
                    log_message = f"检测到进程: {proc_name}, PID: {pid}, 启动时间: {start_time}"
                    print(log_message)
                    write_log(log_message)
                    os.system(f"kill -9 {pid}")
                    write_log(f"已结束进程: {proc_name}, PID: {pid}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        time.sleep(2)

def start_detection(icon):
    global running, paused
    if not running:
        running = True
        paused = False
        thread = threading.Thread(target=detect_and_kill_processes)
        thread.daemon = True
        thread.start()
        icon.notify("检测已开始")
        write_log("检测已开始")
        update_menu(icon)

def pause_detection(icon):
    global paused
    if running and not paused:
        paused = True
        icon.notify("检测已暂停")
        write_log("检测已暂停")
        update_menu(icon)

def resume_detection(icon):
    global paused
    if running and paused:
        paused = False
        icon.notify("检测已继续")
        write_log("检测已继续")
        update_menu(icon)
def stop_detection(icon):
    global running
    if running:
        running = False
        icon.notify("检测已停止")
        write_log("检测已停止")
        icon.stop()

def update_menu(icon):
    if running:
        if paused:
            icon.menu = Menu(
                MenuItem('继续检测', resume_detection, enabled=True),
                MenuItem('暂停检测', pause_detection, enabled=False),
                MenuItem('停止检测', stop_detection)
            )
        else:
            icon.menu = Menu(
                MenuItem('继续检测', resume_detection, enabled=False),
                MenuItem('暂停检测', pause_detection, enabled=True),
                MenuItem('停止检测', stop_detection)
            )
    else:
        icon.menu = Menu(
            MenuItem('开始检测', start_detection),
            MenuItem('继续检测', resume_detection, enabled=False),
            MenuItem('暂停检测', pause_detection, enabled=False),
            MenuItem('停止检测', stop_detection)
        )

def create_tray_icon():
    image = Image.new('RGB', (64, 64), color=(0, 128, 255))
    initial_menu = Menu(
        MenuItem('开始检测', start_detection),
        MenuItem('继续检测', resume_detection, enabled=False),
        MenuItem('暂停检测', pause_detection, enabled=False),
        MenuItem('停止检测', stop_detection)
    )
    icon = Icon("ProcessDetector", image, "多进程检测器", initial_menu)
    icon.run()

if __name__ == '__main__':
    create_tray_icon()
