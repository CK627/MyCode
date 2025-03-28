import time
for zt in range(1, 10):
    for b in range(1, zt + 1):
        time.sleep(0.5)
        print(zt, '×', b, '=', zt * b, end='\t')
    print()
