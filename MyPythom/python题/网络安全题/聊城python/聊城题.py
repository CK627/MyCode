# -*- codeing = utf-8 -*-
# 时间:2021/11/29 19:27
# 作者:CK
# 文件名:聊城题.py
# 开发环境:PyCharm
def dicgenerate():#自定义函数

    n=0#创建变量，计数器，记录一共循环多少次
    l=['r','o','t']#创建一个列表
    f=open('dic.txt','w+')#创建一个dic的文本文件
    for x in l:#for in 循环3次
        for y in l:#for in 循环9次
            for z in l:#for in 循环27次
                for i in l:#for in 循环81次
                    print(x+y+z+i+'\n')#打印x+y+z+i，并换行输出
                    n=n+1#每打印一次，计数器加一
                    f.write(x+y+z+i+'\n')#将x+y+z+i写入文件中，并换行打印
    f.close()#关闭已打开文件
    print(n)#打印n计数器

#dicgenerate()#调用函数