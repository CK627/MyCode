# -*- coding = utf-8 -*-
# @Time:2022/7/6 下午 8:51
# @Author:CK
# @File:代码示例
# @Software:PyCharm
#-*- coding: UTF-8 -*-
import argparse   #步骤一  导库

def parse_args():
    """
    :return:进行参数的解析
    """
    description = "you should add those parameter"                   # 步骤二
    parser = argparse.ArgumentParser(description=description)        # 这些参数都有默认值，当调用parser.print_help()或者运行程序时由于参数不正确(此时python解释器其实也是调用了pring_help()方法)时，
                                                                     # 会打印这些描述信息，一般只需要传递description参数，如上。
    help = "The path of address"
    parser.add_argument('--addresses',help = help)                   # 步骤三，后面的help是我的描述
    args = parser.parse_args()                                       # 步骤四
    return args

if __name__ == '__main__':
    args = parse_args()
    print(args.addresses)            #直接这么获取即可。
