'''
计算地铁票价，输入千米数，输出票价金额。地铁票规定：6KM(含)，内3元；6~12KM(含)4元；12~22KM(含)5元；22~32KM(含)6元；32KM以上部分，每增加1元可乘坐20KM。
'''
km=int(input('输入路程：'))
zt=0
if km<=6:
    zt= km * 3
    print(zt, '元')
elif 6<km<=12:
    zt= 18 + (km - 6) * 4
    print(zt, '元')
elif 12<km<=22:
    zt= 42 + (km - 12) * 5
    print(zt, '元')
elif 22<km<=32:
    zt= 92 + (km - 22) * 6
    print(zt, '元')
else:
    zt= 152 + (km - 32) * (1 / 20)
    print(zt, '元')