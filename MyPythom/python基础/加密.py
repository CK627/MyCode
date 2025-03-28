s=input('请输入一个你要加密的数字：')
s1=''
for a in range(1,50):
    for i in s:
        s1=s1+chr(ord(i)+a)
    print(s1,end="\n")
# print(s1)
# s2=''
# for i in s1:
#     s2=s2+chr(ord(i)-2)
# print(s2)