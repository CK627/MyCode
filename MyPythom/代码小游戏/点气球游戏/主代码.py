from random import *
from turtle import *
from 副代码 import *
balloons = []
size = 50
balloon_colors=["red","black","yellow","blue","green","pink","grey","light blue","light green"]
def distance(a,b,x,y):
    return ((a-x) ** 2 + (b-y) ** 2) ** 0.5
def tap(x,y):
    for n in range(len(balloons)):
        if distance(x,y,balloons[n][0],balloons[n][1])<(size/2):
            balloons.pop(n)
            return
def draw():
    clear()
    for n in range(1,(len(balloons)+1)):
        line(balloons[-n][0],balloons[-n][1],balloons[-n][0],balloons[-n][1]-size*1.5,1)
        up()
        goto(balloons[-n][0],balloons[-n][1])
        dot(size,balloons[-n][2])
        balloons[-n][1]=balloons[-n][1]+1
    for n in range(1,(len(balloons)+1)):
        if balloons[-n][1]>210+size*1.5:
            balloons.pop(-n)
            n=n-1
    update()
def gameLoop():
    if randrange(60)==7:
        x=randrange(-200+size,200-size)
        c=choice(balloon_colors)
        balloons.append([x,-220,c])
    draw()
    ontimer(gameLoop,10)
square(420,420,0,0)
hideturtle()
tracer(False)
listen()
onscreenclick(tap)
gameLoop()
done()