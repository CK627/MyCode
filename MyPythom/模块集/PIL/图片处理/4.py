# -*- coding = utf-8 -*-
# @Time:2022/文件检查文件/文件检查文件 下午 12:40
# @Author:CK
# @File:文件检查文件
# @Software:PyCharm
import time
from subprocess import Popen, PIPE
import threading
threads = []
thread_max = threading.BoundedSemaphore(255)
def ping_check(ip):
    #ip = '127.0.0.1'
    check = Popen('ping {0}\n'.format(ip), stdin=PIPE, stdout=PIPE, shell=True)
    data = check.stdout.read()
    data = data.decode('GBK')
    if 'TTL' in data:
        print('[+] The host {0} is up'.format(ip))
def main(ip):
    # ip = '192.168.1.'
    for i in range(1, 255):
        new_ip = ip + str(i)
        thread_max.acquire()
        t = threading.Thread(target=ping_check, args=(new_ip,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
# 多线程执行
if __name__ == '__main__':
    ip = input("Please input ip (192.168.1.1): ")
    print('[+] Strat scaning......Please wait...')
    start = time.time()
    main(ip[:-1])
    end = time.time()
    print("------------耗时{0:.5f}秒------------".format(end - start))