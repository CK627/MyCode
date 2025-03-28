'''
按要求输出：一共5行，每行10个’*‘。
'''
for zt in range(5):
    for b in range(10):
        print('*',end='')
    print()


zt=0
while zt<5:
    b = 0
    while b<10:
        print('*',end='')
        b=b+1
    print()
    zt = zt + 1
