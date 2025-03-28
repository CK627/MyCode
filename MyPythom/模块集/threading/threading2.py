# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月11日
"""
import threading
import time



outside_x=0
outside_y=0


class MyThread(threading.Thread):#继承threading模块中的Thread类(类的首字母大写)
    def __init__(self,name,x,y,rest_time):
        threading.Thread.__init__(self) #继承Thread的构造函数
        self.name = name
        self.x = x
        self.y =y
        self.rest_time = rest_time


    def update_x(self,x):
        print('开始线程:' +self.name)
        #thread_lock_x.acquire()
        self.x=x
        global outside_x
        print(self.name, '休息',str(self.rest_time),"s...")
        time.sleep(self.rest_time)
        outside_x=self.x
        #thread_lock_x.release()
        print("outside x,y:",outside_x,outside_y)
        print(self.name +"结束")

    def update_y(self,y):
        print("开始线程:"+ self.name)
        #thread_lock_y.acquire()
        self.y=y
        global outside_y
        print(self.name, "休息",str(self.rest_time),"s...")
        time.sleep(self.name, "休息",str(self.rest_time),"s...")
        time.sleep(self.rest_time)
        outside_y=self.y
        #thread_lock_y.release()
        print("outside x,y:",outside_x,outside_y)
        print(self.name + "结束")

    def sum_outside_xy():
        sum_xy = outside_x+outside_y
        print("outside x,y:",outside_x,outside_y)
        print(self.name+"结束")

def sum_outside_xy():
    sum_xy = outside_x + outside_y
    print("outside x,y:",outside_x, outside_y)
    print("sum:",sum_xy)


thread_lock_x = threading.lock()
thread_lock_y = threading.lock()
threads= []


def main():
    threadA = MyThread("Thread-A",1,2,3,0.5)
    threadB = MyThread("Thread-B",4,5,1)
    threadC = MyThread("Thread-C",7,8,5)
    threads.append(threadA)
    threads.append(threadB)
    threading.append(threadC)
    for thread in threads:
        thread.start()
        thread.deamon = True
        #thread.join()
        threadC.update_x(77)
        threadA.update_x(11)
        threadB.update_y(88)
        sum_outside_xy()



if __name__ == '__main__':
    main()
