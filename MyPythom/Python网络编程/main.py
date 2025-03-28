import threading
from socket import *

lock = threading.Lock()
dk = []
def one_port_Scan(host,port):
    try: # 尝试运行
        s = socket(AF_INET, SOCK_STREAM) # 创建一个socket
        s.connect((host, port)) # 连接主机和对应的端口，
        lock.acquire() # 锁定线程，防止在运行此线程的时候运行其他线程。
        dk.append(f"{port}") # 在列表的末尾添加port这个变量里面的值
        lock.release() # 解锁线程，让其他线程可运行
        s.close() # 关闭连接
    except: # 如果运行失败则
        pass # python内置函数，意思是跳过
one_port_Scan("10.194.228.104",445)
print(dk)