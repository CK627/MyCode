from ftplib import FTP

def downloadfile(host):
    ftp = FTP()
    ftp.connect(host,21)
    ftp.login('admin','x7cker')
    bufsize = 1024
    fp = open('output.txt', 'wb')
    ftp.retrbinary(fp.write, bufsize)
    ftp.set_debuglevel(0)
    ftp.close()

downloadfile('tou kan de ren shi gou !!!')