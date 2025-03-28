# -*- coding:utf -8 -*-
"""
作者：Administrator
日期：2021年03月11日
"""
import threading
threading.current_thread()
#添加线程
def thread_job():
         print('This is a thread of %s' % threading.current_thread())

def main():
       thread= threading.Thread(target=thread_job) # 定义线程，常用参数还有args和name，分别是传给target的参数和给这个线程取得名字
       thread.start() #让线程开始工作
       thread.join() #不加join则程序会往下走，尽管线程还没运行完

if __name__ =='__main__':
      main()