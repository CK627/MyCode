import socket


# redis连接
def conn(host, port=6379):
    # 发送一个指令
    payload = 'ping \r\n'
    # 生成一个基于 tcp套接字
    s = __F1__
    # 设置默认连接时长
    socket.setdefaulttimeout(2)
    try:
        # 连接目标机
        s.connect(__F2__)
        # 发送一个指令
        s.send(__F3__)
        # 接收回显的数据，根据这个数据判断是否是未授权
        # 需要数字时，使用1024代替
        recv_data = __F4__
        # 关闭连接对象
        __F5__
        if recv_data and 'PONG' in recv_data:
            __F6__ '存在redis未授权'
        return f'{host}:{port} 不存在redis未授权'
    except:
        # 连接超时
        return f'{host}:{port} 连接超时'


if __name__ == '__main__':
    print(conn('49.232.27.45', 6379))
    print(conn('50.区块链式随机.164.49', 6379))


