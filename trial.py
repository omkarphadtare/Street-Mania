import pygame
import time
import random

pygame.init()
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
darkred=(255,0,0)
green=(0,200,0)
darkgreen=(0,255,0)
width=800
height=600
car_width=78 #car_width=75
car_height=148 #car_height=100
x1_width=75 #x1_width=80
y1_height=145 #y1_height=110
gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption('Street Mania')
clock=pygame.time.Clock()
carImg=pygame.image.load('sed1.png')
carImg1=pygame.image.load('sed2.png')
back=pygame.image.load('road1.jpg')
pygame.display.set_icon(carImg1)  #optimal size should be 32x32
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
def car1(x1,y1):
    gameDisplay.blit(carImg1,(x1,y1))
    
def crashed():
    msg("You Crashed!")
    
def msg(text):
    Text=pygame.font.Font(None, 80)
    TextSurf, TextRect = text_objects(text, Text)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def scoreboard(score):
    font=pygame.font.SysFont(None, 35)
    text=font.render("Score: "+str(score), True, white)
    gameDisplay.blit(text, [5,5])

def button(text,x,y,w,h,ic,ac):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x<mouse[0]<x+w and y<mouse[1]<y+h:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0]==1 and text=="Play":
            game_loop()
        elif  click[0]==1 and text=="Quit":
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))        
        
    Text=pygame.font.Font(None, 40)
    TextSurf, TextRect = text_objects(text, Text)
    TextRect.center = ( (x+(w/2)),(y+(h/2)) )
    gameDisplay.blit(TextSurf, TextRect)
    
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)                
        Text=pygame.font.Font(None, 80)
        TextSurf, TextRect = text_objects("Street Mania", Text)
        TextRect.center = ((width/2),(height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Play",150,475,100,50,darkgreen,green)
        button("Quit",550,475,100,50,darkred,red)
        pygame.display.update()
        clock.tick(15)
        
def game_loop():
    pygame.mixer.music.load('alone_marshmello.mp3')
    pygame.mixer.music.play(-1)
    x=(width * 0.45)
    y=(height * 0.75)
    x1=random.randrange(0, width)
    y1=(height * 0.05)
    x_change=0
    y_change=0
    y1_change=0
    score=0
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    y1_change= 7
                    x_change= -7
                if event.key == pygame.K_RIGHT:
                    y1_change= 7
                    x_change= 7
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change=0
                    y_change=0
        x+=x_change
        y+=y_change
        y1+=y1_change
        gameDisplay.blit(back,[0,0])
        #gameDisplay.fill(white)
        car(x,y)
        car1(x1,y1)
        scoreboard(score)
        
        if x> width - car_width or x< -25:
            x_change=0
            crashed()
           # pygame.mixer.music.pause(music)
            
        if y1> height:
            y1=0
            x1=random.randrange(0, width)
            score+=1
            y1_change+=0.5
        '''if y < y1+110 and y1+110 < y+car_height:
            if x > x1 and x < x1+35 or x1 < x+car_width and x+car_width < x1+35 or x1+35 == x:
                crashed()'''
        
        if y < y1+y1_height and y1+110 < y+car_height:
            if x > x1 and x < x1+x1_width or x+car_width > x1 and x + car_width < x1+x1_width:
                crashed()        
        pygame.display.update()
        clock.tick(90)
        
game_intro()
game_loop()
pygame.quit()
quit()    