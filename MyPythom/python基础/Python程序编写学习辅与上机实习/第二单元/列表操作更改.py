list1=[100,200,300,'student','teacher']
list2=['a1','b1','c1','d1','e1']
list3=[list2,[12,343]]
list4=[list1,list2]
print(list1)
print(list4)
list1[1]='b'
list2[0:2]=1,2,3
del list3[0]
print(list1)
print(list2)
print(list3)
