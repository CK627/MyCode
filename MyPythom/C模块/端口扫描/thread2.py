import thread,time
from socket import *

def socket_port(ip,port):
        try:
            s=socket(AF_INET, SOCK_STREAM)
            result=s.connect_ex((ip,port))
            if result==0:
                lock.acquire()
                print ('[+]'+str(port)+'/tcp open')
                lock.release()
        except:
            print( "fail")
            s.close
def ip_scan(ip):
        try:
                print ('start scan',ip)
                for i in range(1,1024):
                    thread.start_new(socket_port,(ip,int(i)))
                time.sleep(0.01)
                print ('OK')
                raw_input("Enter to exit")
        except:
                print ("fail to scan")

if __name__=='__main__':
    url=raw_input('input the ip you want to scan:')
    lock=thread.allocate()
    ip_scan(url)