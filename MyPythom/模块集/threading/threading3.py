# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月12日
"""
import threading
global_n =0

def job1():
    global global_n
    for i in range(10):
        global_n += 10
        print('jib2',global_n)

def job2():
    global global_n
    for i in range(10):
        global_n +=10
        print('job2',global_n)


    t1=threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    # t1.join()  #这里join与否都可能会乱序
    # t2.join()
