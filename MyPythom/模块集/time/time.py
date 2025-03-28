import time
while True:
    time.sleep(1)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# while True:
#     a = input('请输入‘1’退出：')
#     if a == '1':
#         break
