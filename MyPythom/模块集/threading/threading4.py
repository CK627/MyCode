# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月12日
"""
import threading

thread_lock_n=threading.Lock()


def job1():
    global global_n
    thread_lock_n.acquire()
    for i in range(10):
        global_n += 1
        print('job1',global_n)
        thread_lock_n.release()


def job2():
    global global_n
    thread_lock_n.acquire()
    for i in range(10):
        global_n += 10
        print('job2', global_n)

    thread_lock_n.release()
