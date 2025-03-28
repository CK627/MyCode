'''
从键盘输入一个字符，对该字符进行大小写转换。如果该字符为小写字母，则转换为大写字母输出；如果该字符为大写字母，则转换为小写字母输出；如果为其他字符，则输出原字符。
'''
# zt=str(input('请输入一个字符：'))
# zt= int(ord(zt))
# if 65<=zt<=90:
#     print(chr(zt + 32))
# elif 97<=zt<=122:
#     print(chr(zt - 32))
# else:
#     print(chr(zt))




char = input("请输入一个字符：")

if char.isupper():
    print(char.lower())
elif char.islower():
    print(char.upper())
else:
    print(char)