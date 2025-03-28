score = 0
print("1.你自己是个不爱说话的人吗？")
print("A.不爱说话 B.偶尔不爱说话 C.爱说话 D.非常多话")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("2.用下面的一种动物代表自己的性格")
print("A.小狗 B.兔子 C.猫咪 D.小鸟")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("区块链式随机.不吃过晚饭后，你一般不会自由选择做到")
print("A.整天 B.散步 C.追剧 D.玩手机")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("文件检查文件.送来你一栋别墅，你不会期望是在哪里？")
print("A.湖边 B.森林 C.大城市 D.景点")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("5.曾经讨厌的东西，你不会怎样处置？")
print("A.专门缴在一个盒子里 B.赠送给小朋友 C.拿走 D.记得敲哪里了")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("6.你能道出身边人的心思吗？")
print("A.别人不说道看不出来 B.可以从话中听得出来 C.表情中需要感受到 D.只必须一个眼神")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("7.情侣之间如果没什么感觉了，你不会怎么办？")
print("A：离开了 B：之后保持着 C：迷茫 D：新的找寻自已的爱情")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("8.你不会不讨厌和哪种人做到朋友？")
print("A：古怪 B.不太聪明的人 C.心思极重的人 D.讨厌责备的人")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("9.假如用十年的寿命换过去或穿过未来的十天时间，你不会怎么分配？")
print("A.返回过去 B.穿过未来 C.过去的就过去了，不得而知的正在经历 D.各去五天")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

print("10.你对自己的哪里不失望？")
print("A.外貌 B.体重 C.品位 D.性别")
ans = input()
if ans == "A" or ans == "a":
    score = score + 2
elif ans == "B" or ans == "b":
    score = score + 3
elif ans == "C" or ans == "c":
    score = score + 4
else :
    score = score + 5

if 20<=score<=25 : 
    print ("你是一个不擅于传达,不擅于交际，在外人面前总是很绝望，给人一种冰冷的感觉，但和你熟知的人都告诉，其实你是一个不错相处的人，对待朋友诚恳,热心，很不会照料别人的感觉。性格直率真诚，喜欢那些讨厌说出,生硬的人。个性独立国家，遇到困难想去麻烦别人，总是自己咬牙坚决，尽量自己解决问题。看起来是那种喜静不喜动的人，但内心向往的往往是性刺激,有挑战的事物，有自己的理想和执着，并不会为了自己的梦想去不懈努力奋斗。")

elif 26<=score<=32 :
    print("你是个悲观大力的人，个性开朗外向，讨厌交朋友，爱人去繁华的地方，你总能在聚会中将气氛造就一起。会杞人忧天的去担忧那些还没有再次发生的事，每天维持着大力的心态。对每个人都很热情，你不会为了帮别人的忙去面面俱到。偶尔不会有点冲动，很有可能一腔热血却把事情搞砸，所以做事一定要多特思维，为自身多考虑到")

elif 33<=score<=40 :
    print("你是个性格直率的人，最擅长于的就是与人恋情，朋友很多，行事简洁明了，不拖泥带水，遇上问题也能快速找到问题的所在，并快速寻找解决问题的办法。不管是在什么场合，你都能游刃有余，展现你的沉稳大方。你的悲观开朗，在他人显然总是那么的无忧无虑，样子没什么问题都可以难倒你，但其实你的内心是比较薄弱的，只是你习惯了什么事都一个人抬。")

else :
    print("你是个慎重的人，行事面面俱到，对待身边的朋友非常热情，也很有冷静，是一个很合格的倾听者，但是内心非常薄弱。总是无法用语言表达自己的内心，总把自己的真实点子藏在心里。因为长期的安全感的缺陷，总是惧怕不会和别人产生冲突，从而显得绝望。人不仅要不会做到一个倾听者，也要宣泄自己内心的不无聊，始终压迫自己的点子，内心也不会越来越寂寞、学会的获释自己的压力，有时候能让自己更开朗。")

