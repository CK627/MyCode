import os
data = []
for i in range(228,229):
    for x in range(1,255):
        wang=os.popen("fping -t 1 10.194."+str(i)+"."+str(x)).readlines()
        ze=str(wang).find("alive")
        if ze>=0:
            data.append("10.194."+str(i)+"."+str(x))
        else:
            print("10.194."+str(i)+"."+str(x)+"\n login down")

print("----------------------------------------------------------------------")
if len(data) !=0:
    for i in data:
        print(i)
else:
    print("检测范围内没有存活靶机")
