import base64
zt= 'll'
str2=base64.encodebytes(zt.encode('utf-8'))
print(str2.decode(),end='')
str1='bGw='
temp=base64.b64decode(str1)
print(temp.decode(),end='')

