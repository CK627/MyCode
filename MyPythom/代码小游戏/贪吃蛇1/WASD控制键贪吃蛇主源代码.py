#####################引用数据库与函数#####################
from turtle import *
from WASD控制键贪吃蛇副源代码 import square
from random import randrange
from time import sleep
#########################定义变量#########################
snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
apple_x=randrange(-20,18)*10
apple_y=randrange(-19,19)*10
aim_x=0
aim_y=10
#########################定义函数#########################
def change(x,y):
    global aim_x,aim_y
    aim_x=x
    aim_y=y

def inside_snake():
    for n in range(len(snake)-1):
        if snake[-1][0] == snake[n][0] and snake[-1][1]==snake[n][1]:
            return True

    return False

def inside_map():
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True 
    else : 
        return False 

def gameLoop():
    global apple_x,apple_y,aim_x,aim_y,snake  
    snake.append([ snake[-1][0]+aim_x , snake[-1][1]+aim_y ])
    
    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else :
        apple_x=randrange(-20,18)*10
        apple_y=randrange(-19,19)*10

    if (not inside_map()) or inside_snake():
        square(snake[-1][0],snake[-1][1],10,"red")
        update()
        sleep(2)
        snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
        apple_x=randrange(-20,18)*10
        apple_y=randrange(-19,19)*10
        aim_x=0
        aim_y=10 
    
    clear()
    square(-210,-200,410,"black")
    square(-200,-190,390,"white")
    square(apple_x,apple_y,10,"red")
    for n in range(len(snake)):
        square(snake[n][0],snake[n][1],10,"black")
    update()
    ontimer(gameLoop,200)
    
##########################主程序##########################
square(420,420,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(0,10),"w")
onkey(lambda: change(0,-10),"s")
onkey(lambda: change(-10,0),"a")
onkey(lambda: change(10,0),"d")
gameLoop()
done()