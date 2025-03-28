from scapy.all import *
conf.verb=0
ip=input('请输入要扫描的ip地址：')
lport=input('输入你要扫描的起始端口：')
hport=input('输入你要扫描的结束端口：')
for i in range(int(lport),int(hport)):
    pkt=IP(dst=ip)/TCP(dport=i)
    ans,uans=sr(pkt)
    res=str(ans[0])
    print(res)
    if re.findall('SA',res):
        print(str(i)+'yes')
    else:
        pass