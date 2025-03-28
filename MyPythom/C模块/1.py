# -*- coding = utf-8 -*-
# @Time:2024/8/14 09:42
# @Author:ck
# @File:1
# @Software:PyCharm
import flag,key

assert(len(key) == 5)
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{_}"
w ={}
for i in range(len(letter)):
    l = letter[i:]+letter[:i]
    dic = {}
    for j in range(len(l)):
        dic[letter[j]] = l[j]
    w[letter[i]] = dic

def encrypt(m,key):
    x1 = len(m)//len(key)
    x2 = len(m)%len(key)
    key += x1*key + key[0:x2]
    c = ""
    print(len(m))
    print(len(key))

    for i in range(len(m)):
        c += w[m[i]][key[i]]
    return c

c =  encrypt(flag,key)
print(c)

#DKQ6NFHDW33MAW9B}4UV1OB0{7G7VU8C1U3CO6V6
