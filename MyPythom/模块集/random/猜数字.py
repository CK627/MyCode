import random # 导入random这个模块
zt=random.randint(1, 100) # 随机取1~100之间的数，并存储进常量a中
f=0 # 创建一个变量
while f==0: # while循环，循环一次
    b=int(input("请输入一个1到100之间的整数:")) # 自定义一个变量
    if b==zt: # 假如自定义的变量等于随机的常量
        print('恭喜你猜对了') # 打印结果
        break # 结束运行
        # f==1 # 为了连续第二次循环，使while循环进行下一次循环（可有可无，不影响运行）
    elif b<zt: # 如果否则自定义的变量小于随机的常量
        print('小了') # 打印结果
    else: # 否则
        print('大了') #打印结果
        
