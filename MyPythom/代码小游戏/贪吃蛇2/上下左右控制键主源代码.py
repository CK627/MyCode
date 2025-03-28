import pygame
import time
import random

pygame.init()

step=10
init_len=8
map_width=500
map_height=400
FPS=5
direction = 'up'
snake_x=[]
snake_y=[]

gameScreen = pygame.display.set_mode((map_width,map_height))
clock=pygame.time.Clock()


white=(255,255,255)
black=(0,0,0)
green=(0,155,0)
red  =(255,0,0)

pygame.display.set_caption("Snake Game")
img = pygame.image.load("head.png")
app = pygame.image.load("apple.png")

def setupSnake():
    snake_x.clear()
    snake_y.clear()
    for n in range(init_len):
        snake_x.append(map_width/2)
        snake_y.append(map_width/2+(init_len-n-1)*step)

def drawMap():
    gameScreen.fill(black,rect = (0,0,map_width,step))
    gameScreen.fill(black,rect = (0,0,step,map_height))
    gameScreen.fill(black,rect = (0,map_height-step,map_width,step))
    gameScreen.fill(black,rect = (map_width-step,0,step,map_height))

def message_to_screen(msg,type=black):
    font = pygame.font.SysFont(None,25)
    screen_text = font.render(msg,True,type)
    gameScreen.blit(screen_text,[(map_width/2)-(len(msg))*4,map_height/2-10])
    pygame.display.update()

def insideSnake(x,y):
    for n in range(len(snake_x)):
        if x==snake_x[n] and y==snake_y[n]: return True
    return False

def drawSnake():
    head = img
    if direction == 'up':       head = img
    if direction == 'down':     head = pygame.transform.rotate(img,180)
    if direction == 'right':    head = pygame.transform.rotate(img,270)
    if direction == 'left':     head = pygame.transform.rotate(img,90)
    gameScreen.blit(head,(snake_x[-1],snake_y[-1]))
    for n in range(len(snake_x)-1):     
        pygame.draw.rect(gameScreen,black,(snake_x[n],snake_y[n],step,step))
    

def gameLoop():
    pygame.init()
    global direction
    gameclose = False
    gameOver = False
    lead_x_change = 0
    lead_y_change = -step
    apple_x = (random.randrange(step,map_width-step)//step)*step
    apple_y = (random.randrange(step,map_height-step)//step)*step
    global snake_x
    global snake_y
    snake_x.clear()
    snake_y.clear()
    pygame.init()
    setupSnake()
    while not gameclose:
        pygame.init()
        if gameOver==True:
            pygame.init()
            message_to_screen("You Lose",red)

            time.sleep(2)
            pygame.display.update()
            gameScreen.fill(white)
            message_to_screen("Game over, press enter to play again")
            pygame.display.update()
        while gameOver==True:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:       pygame.quit() 
                elif event.type == pygame.KEYDOWN:  gameLoop()

        for event in pygame.event.get():
            ##print(event)
            if event.type == pygame.QUIT:           gameclose=True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:      lead_x_change = -step;   lead_y_change = 0; direction = 'left'
                elif event.key == pygame.K_RIGHT:   lead_x_change = step;    lead_y_change = 0; direction = 'right'
                elif event.key == pygame.K_UP:      lead_y_change = -step;   lead_x_change = 0; direction = 'up'
                elif event.key == pygame.K_DOWN:    lead_y_change = step;    lead_x_change = 0; direction = 'down'
                else :                              lead_y_change = 0;       lead_x_change = 0
        lead_x = snake_x[len(snake_x)-1]
        lead_y = snake_y[len(snake_y)-1]
        gameScreen.fill(white)
        drawMap()
        gameScreen.blit(app,(apple_x,apple_y))
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        if lead_x>=map_width-step or lead_x<=0 or lead_y>=map_height-step or lead_y<=0 or (lead_x_change!=lead_y_change and insideSnake(lead_x,lead_y)):
            gameOver=True
            for n in range(len(snake_x)):     
                pygame.draw.rect(gameScreen,black,(snake_x[n],snake_y[n],step,step))
            pygame.draw.rect(gameScreen,red,(lead_x,lead_y,step,step))
            pygame.display.update()
        if not gameOver:
            snake_x.append(lead_x)
            snake_y.append(lead_y)
            if apple_x==lead_x and apple_y==lead_y:
                while(insideSnake(apple_x,apple_y)):
                    apple_x = (random.randrange(step,map_width-step)//step)*step
                    apple_y = (random.randrange(step,map_height-step)//step)*step
                gameScreen.blit(app,(apple_x,apple_y))
            elif lead_x_change==lead_y_change:   
                snake_x.pop(-1)
                snake_y.pop(-1)    
            elif lead_x_change!=lead_y_change:   
                snake_x.pop(0)
                snake_y.pop(0)
            drawSnake()
            pygame.display.update()
            clock.tick(FPS)
    pygame.quit()

pygame.init()
gameLoop()