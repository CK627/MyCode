from turtle import *
from 副源代码 import *
from random import randrange 
from time import sleep
writer = Turtle(visible = False)

contact=1              #contact 每天接触人数
infected=5              #infected 最初感染人数
inf_p=0.1               #inf_p 接触感染者后感染概率
cure_p=0.2              #cure_p 每天康复概率
dead_p=0.02             #deap_p 每天死亡概率
population = 500        #population 总人口
hospital = 50            #hospital 床位

dead=0
recovered=0
aline=100
normal = []
recovery = []
sick = []
death = []
day = 1
def message():
    writer.clear()
    writer.up()
    writer.goto(220,200)
    writer.color('black')
    writer.down()
    writer.write("Contact = {}".format(contact),font=("Arial" , 20 , "normal"))
    writer.up()
    writer.goto(220,160)
    writer.color('black')
    writer.down()
    writer.write("Infected = {}%".format(round(infected/population*100,1)),font=("Arial" , 15 , "normal"))
    writer.up()
    writer.goto(220,120)
    writer.color('black')
    writer.down()
    writer.write("Dead     = {}%".format(round(dead/population*100,1)),font=("Arial" , 15 , "normal"))
    writer.up()
    writer.goto(220,0)
    writer.color('black')
    writer.down()
    writer.write("    Day {}    ".format(day),font=("Arial" , 20 , "normal"))
    update()

def initialise():
    square(820,620,0,0)
    hideturtle()
    tracer(False)

    line(-300-aline,300,300-aline,300)
    line(-300-aline,300,-300-aline,-300)
    line(300-aline,-300,300-aline,300)
    line(300-aline,-300,-300-aline,-300)

def loadMap():
    message()
    for n in range(population-infected-recovered):
        x=randrange(-300-aline,300-aline-20)
        y=randrange(-300,300-20)
        while [x,y] in normal:
            x=randrange(-300-aline,300-aline-20)
            y=randrange(-300,300-20)
        normal.append([x,y])
    for n in range(infected):
        x=randrange(-300-aline,300-aline-20)
        y=randrange(-300,300-20)
        while [x,y] in normal:
            x=randrange(-300-aline,300-aline-20)
            y=randrange(-300,300-20)
        sick.append([x,y])
    for n in range(population-infected-dead-recovered):
        square(normal[n][0],normal[n][1],20,"green")
    for n in range(recovered):
        square(recovery[n][0],recovery[n][1],20,"green")   
    for n in range(infected):
        square(sick[n][0],sick[n][1],20,"red")
    for n in range(dead):
        square(death[n][0],death[n][1],20,"black")
    update()

def begin():
    global infected,dead,recovered,day
    #print("infected={},dead={},recovered={}".format(infected,dead,recovered))
    if hospital>infected : inbed=infected 
    else : inbed = hospital 
    for i in range(inbed):
        p=randrange(0,100)
        if p<=100*cure_p:
           # print("infected={},dead={},recovered={}".format(infected,dead,recovered))
            recovery.append(sick[i])
            sick.pop(i)
            recovered = recovered + 1
            infected = infected -1
    for i in range(infected):
        p=randrange(0,100)
        if p<=100*dead_p:
           # print("infected={},dead={},recovered={}".format(infected,dead,recovered))
            death.append(sick[i])
            sick.pop(i)
            dead = dead + 1
            infected = infected -1
        #print("infected={},dead={},recovered={}".format(infected,dead,recovered))
    for i in range(infected):
        for c in range(contact):
            if (population-infected-dead-recovered)>0 :
             #   print("infected={},dead={},recovered={}".format(infected,dead,recovered))
                n=randrange(0,population-infected-dead-recovered)
                p=randrange(0,100)
                if p<=100*inf_p:
                    sick.append(normal[n])
                    normal.pop(n)
                    infected = infected + 1
    day = day + 1
    loadMap()
    if infected ==0 : return 
    ontimer(begin,300)
    


initialise()
message()
loadMap()
sleep(1)
listen()
onkey(lambda:begin(),'s')
update()
done()
