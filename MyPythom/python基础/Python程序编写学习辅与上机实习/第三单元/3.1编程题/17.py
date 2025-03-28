'''
计算学生平均分。从键盘输入一位学生某次考试的语文、数学、英语成绩，计算这位学生成绩的平均分，并输出结果。
'''
ls=['语文','数学','英语']
for i in range(len(ls)):
    zt=int(input('请输入这位学生的{}成绩:'.format(ls[i])))
    ls.append(zt)
    del ls[0]
print(sum(ls)/len(ls))