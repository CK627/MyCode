a=int(input("a:"))
b=int(input("b:"))
c=int(input("C:"))
if a+b>c and a+c>b and b+c>a:
    print("三角形的周长是：",a+b+c)
else:
    print("不能成为三角形")