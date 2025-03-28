# -*- coding = utf-8 -*-
# @Time: 2022/1/615:17
# @Author： CK
# @File: 计算电费
# @Software: PyCharm
n1=int(input('请输入本月（峰）用电数：'))
n2=int(input('请输入本月（谷）用电数：'))
v1=(n1+n2)*0.538
v2=n1*0.568+n2*0.288
v3=12*(v1-v2)
print('传统用电计费，付：',round(v1,1),'元')
print('峰谷电计费，付：',round(v2,1))
print('一年下来，峰谷电节省',round(v3,1),'元')