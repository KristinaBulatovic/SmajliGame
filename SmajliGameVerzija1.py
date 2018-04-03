import pygame
import time
import random

pygame.init()

#crash_sound = pygame.mixer.Sound("Crash.wav")
#pygame.mixer.music.load("jazz.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

yellow = (251,238,0)
pink = (255,85,170)

bright_yellow = (255,255,0)
bright_pink = (255,0,128)

block_color = (239,109,177)

smajli_width = 68

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Smajli Game')
clock = pygame.time.Clock()

smajliImg = pygame.image.load('smajli.png')
gameIcon = pygame.image.load('smajli1.png')

pygame.display.set_icon(gameIcon)

pause = False

def things_score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def smajli(x,y):
    gameDisplay.blit(smajliImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

##def message_display(text):
##    largeText = pygame.font.SysFont("comicsansms",115)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
##
##    pygame.display.update()
##
##    time.sleep(2)
##
##    game_loop()
    
def crash():

    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Game Over", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)

        button("Play Again",150,450,100,50,yellow,bright_yellow,game_loop)
        button("Quit",550,450,100,50,pink,bright_pink,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
def paused():

    #pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)

        button("Continue",150,450,100,50,yellow,bright_yellow,unpause)
        button("Quit",550,450,100,50,pink,bright_pink,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Smajli Game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY",150,450,100,50,yellow,bright_yellow,game_loop)
        button("Quit",550,450,100,50,pink,bright_pink,quitgame)
        
        pygame.display.update()
        clock.tick(15)
    
def game_loop():
    global pause

    #pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 30
    thing_height = 30

    thingCount = 1

    score = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        smajli(x,y)
        things_score(score)
        
        if x > display_width - smajli_width or x < 0:
            crash ()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            score += 1
            thing_speed += 0.5
            thing_width += 1
            thing_height += 1

        if y < thing_starty + thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x + smajli_width > thing_startx and x + smajli_width < thing_startx + thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
