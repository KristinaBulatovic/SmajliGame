import pygame
import time
import random
import math

pygame.init()
crash_sound = pygame.mixer.Sound("Crash.mp3")
pygame.mixer.music.load("A_Long_Cold.mp3") 

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

yellow = (251,238,0)
pink = (255,85,170)
green = (81,165,18)
blue = (17,151,215)

bright_yellow = (255,255,0)
bright_pink = (255,0,128)
bright_green = (98,201,22)
bright_blue = (105,199,243)

boja1,boja2,boja3,boja4 = (239,109,177),(239,109,177),(239,109,177),(239,109,177)

smajli_width = 68

score = 0
brojZivota = 4
dal = False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Smajli Game')
clock = pygame.time.Clock()

smajliImg = pygame.image.load('smajli.png')
gameIcon = pygame.image.load('smajli1.png')

pygame.display.set_icon(gameIcon)

pause = False

def zivoti():
    global brojZivota
    zivot = pygame.image.load('srce.png')
    if(brojZivota>1): gameDisplay.blit(zivot,(760,0))
    if(brojZivota>2): gameDisplay.blit(zivot,(730,0))
    if(brojZivota>3): gameDisplay.blit(zivot,(700,0))

def things_score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

def get_high_score():
    high_score = 0
 
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        print("There is no high score yet.")
    except ValueError:
        print("I'm confused. Starting with no high score.")
 
    return high_score

def save_high_score(new_high_score):
    try:
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        print("Unable to save the high score.")

def main():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
        
    high_score = get_high_score()
    gameDisplay.fill(white)

    font = pygame.font.SysFont("comicsansms", 100)
    text = font.render("High Score:", True, yellow)
    Score = font.render(str(high_score), True, pink)
    gameDisplay.blit(text,(125,100))
    gameDisplay.blit(Score,(325,240))

    highScore = True

    while highScore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        global dal
        button("Play Again",100,450,100,50,white,white,game_loop,dal)
        button("Quit",600,450,100,50,white,white,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def smajli(x,y):
    gameDisplay.blit(smajliImg,(x,y))
    #gameDisplay.blit(smajliImg,(x+display_width,y))
    #gameDisplay.blit(smajliImg,(x-display_width,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def crash(nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty):
    global brojZivota
    brojZivota -= 1
    print(brojZivota)
    if(brojZivota < 1):

        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Game Over", largeText,)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        high_score = get_high_score()
        current_score = 0
        try:
            current_score = score
        except ValueError:
            print("I don't understand what you typed.")
     
        if current_score > high_score:
            print("Yea! New high score!")
            save_high_score(current_score)
        else:
            print("Better luck next time.")

        while True:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            global dal
            button("Play Again",100,450,100,50,yellow,bright_yellow,game_loop, dal)
            button("Back",250,450,100,50,blue,bright_blue,game_intro)
            button("HighScore",400,450,100,50,green,bright_green,main)
            button("Quit",550,450,100,50,pink,bright_pink,quitgame)
            
            pygame.display.update()
            clock.tick(15)
    else:
            print("Ovde smo")
            x = (display_width/2) - (smajli_width/2)
            y = (display_height/2) - (smajli_width/2)
            a,b,c,d,e,f,thing_startx, thing_starty = -1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000
    
            level(nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty)     

def button(msg,x,y,w,h,ic,ac,action=None,dal=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if(dal != None): action(dal)
            else: action()
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
    global pause

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    clock.tick(15)

    while pause:
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    unpause()
                

        button("Continue",150,450,100,50,yellow,bright_yellow,unpause)
        button("Quit",550,450,100,50,pink,bright_pink,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def game_intro():
    while True:
            pygame.event.get()
            click = pygame.mouse.get_pressed()
            print(click)
            if(not click[0] == 1):
                break
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
        
        button("PLAY",100,450,100,50,yellow,bright_yellow,game_loop,True)
        button("YALP",250,450,100,50,blue,bright_blue,game_loop,False)
        button("HighScore",400,450,100,50,green,bright_green,main)
        button("Quit",550,450,100,50,pink,bright_pink,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def tackaOdTacke(x1, x2, y1, y2):
    ret = math.sqrt((x2-x1) * (x2-x1)  + (y2-y1) * (y2-y1))
    return ret
def linijaSaKrugom(x1,x2,y1,y2,centarX,centarY,r):
    if(y1 >= centarY - r + 2 and y2 <= centarY + r - 2):
        if(x1 < centarX and x2 > centarX):
            return True
    return False
#x1,y1 --> manja tacka linije
#x2,y2 --> veca tacka linije
#centarX, centarY --> krug

def sudarKrugI4tacke(x1,x2,x3,x4,y1,y2,y3,y4, centarX, centarY,r):
    if((tackaOdTacke(x1,centarX, y1, centarY) < r) or
        (tackaOdTacke(x2,centarX, y2, centarY) < r) or
        (tackaOdTacke(x3,centarX, y3, centarY) < r) or
        (tackaOdTacke(x4,centarX, y4, centarY) < r)or
        linijaSaKrugom(x3,x4,y3,y4,centarX,centarY,r)or #donja crta
        linijaSaKrugom(x1,x2,y1,y2,centarX,centarY,r)or #gornja crta
        linijaSaKrugom(y1,y3,x1,x3,centarY,centarX,r)or #levo
        linijaSaKrugom(y2,y4,x2,x4,centarY,centarX,r)): #desno
        return True
    return False

def TekstZaNivo(tekst):
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects(tekst, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(1)

def nastavak():
    global score

    x = (display_width/2) - (smajli_width/2)
    y = (display_height/2) - (smajli_width/2)
    a,b,c,d,e,f,thing_startx, thing_starty = -1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000
    while True:
        if(score == 5):
            TekstZaNivo("Level 2")
            x,y,a,b,c,d,e,f,thing_startx, thing_starty = level(2, 15, x,y,a,b,c,d,e,f,thing_startx, thing_starty)
        elif(score == 15):
            TekstZaNivo("Level 3")
            x,y,a,b,c,d,e,f,thing_startx, thing_starty = level(3, 31, x,y,a,b,c,d,e,f,thing_startx, thing_starty)
        elif(score > 30):
            TekstZaNivo("Level 4")
            x,y,a,b,c,d,e,f,thing_startx, thing_starty = level(4, 1500, x,y,a,b,c,d,e,f,thing_startx, thing_starty)
        else:
            TekstZaNivo("Level 1")
            x,y,a,b,c,d,e,f,thing_startx, thing_starty = level(1, 5, x,y,a,b,c,d,e,f,thing_startx, thing_starty) 
        
        
    pygame.display.update()
    clock.tick(60)
    
def game_loop(dalL):
    global score
    global brojZivota
    global dal
    dal = dalL
    score = 0
    brojZivota = 4

    
    while True:
        x = (display_width/2) - (smajli_width/2)
        y = (display_height/2) - (smajli_width/2)
        a,b,c,d,e,f,thing_startx, thing_starty = -1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000

        if(score == 5):
            TekstZaNivo("Level 2")
            level(2, 15, x,y,a,b,c,d,e,f,thing_startx, thing_starty)
        elif(score == 15):
            TekstZaNivo("Level 3")
            level(3, 31, x,y,a,b,c,d,e,f,thing_startx, thing_starty)
        elif(score > 30):
            TekstZaNivo("Level 4")
            level(4, 1500, x,y,a,b,c,d,e,f,thing_startx, thing_starty)
        else:
            TekstZaNivo("Level 1")
            level(1, 5, x,y,a,b,c,d,e,f,thing_startx, thing_starty) 
        
        
    pygame.display.update()
    clock.tick(60)
def novaBoja():
    return (random.randrange(255),random.randrange(255),random.randrange(255))
def level(nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty):
    
    global pause
    global score
    global boja1,boja2,boja3,boja4
    print(nivo, kad, score)

    global dal
    if(dal): tina = 1
    else: tina = -1

    pygame.mixer.music.play(-1)
    
    #x = (display_width/2) - (smajli_width/2)
    #y = (display_height/2) - (smajli_width/2)

    x_change = 0
    y_change = 0

    thing_width = 30
    if(thing_startx == -1000):
        thing_startx = random.randrange(0, display_width-thing_width)
        thing_starty = -100
    thing_speed = 5
    thing_height = 30

    if(nivo > 1 and a == -1000):
        a = random.randrange(0, display_width-thing_width)
        b = 700
    if(nivo > 2 and c == -1000):
        c = -100
        d = random.randrange(0, display_height-thing_height)
    if(nivo > 3 and e == -1000):
        e = 900
        f = random.randrange(0, display_height-thing_height)

    thingCount = 1

    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 * tina
                if event.key == pygame.K_RIGHT:
                    x_change = 5 * tina
                if event.key == pygame.K_UP:
                    y_change = -5 * tina
                if event.key == pygame.K_DOWN:
                    y_change = 5 * tina
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                  
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, boja1)
        things(a, b, 30, 30, boja2)
        things(c, d, 30, 30, boja3)
        things(e, f, 30, 30, boja4)
        
        thing_starty += thing_speed
        if(nivo > 1):
            b -= thing_speed
        if(nivo > 2):
            c += thing_speed
        if(nivo > 3):
            e -= thing_speed
        
        smajli(x,y)
        things_score(score)
        zivoti()
        r = smajli_width/2

        
        
#        if x > display_width:
#            x = 0
#        if x + smajli_width < 0:
#            x = display_width - smajli_width

        if x > display_width - smajli_width or x < 0 or y > display_height - smajli_width or y < 0:
            crash (nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width-thing_width)
            #thing_speed += 0.5
            #thing_width += 1
            #thing_height += 1
            score += 1
            boja1 = novaBoja()

        if b < 0 and nivo > 1:
            b = display_height
            a = random.randrange(0, display_width-thing_width)
            score += 1
            boja2 = novaBoja() 

        if c > display_width and nivo > 2:
            c = 0 - thing_width
            d = random.randrange(0, display_height-thing_height)
            score += 1
            boja3 = novaBoja()

        if e < 0 and nivo > 3:
            e = display_width
            f = random.randrange(0, display_height-thing_height)
            score += 1
            thing_speed += 0.1
            boja4 = novaBoja()

        r = smajli_width / 2
        centarX = x + r
        centarY = y + r
        

        x1 = thing_startx #levo gore
        x2 = thing_startx + thing_height#desno gore
        x3 = thing_startx #levo dole
        x4 = thing_startx + thing_height#desno dole
        y1 = thing_starty
        y2 = thing_starty
        y3 = thing_starty + thing_width 
        y4 = thing_starty + thing_width 

        if(sudarKrugI4tacke(x1,x2,x3,x4,y1,y2,y3,y4, centarX, centarY,r)):
            crash(nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty)
        if(sudarKrugI4tacke(a,a+30,a,a+30,b,b,b+30,b+30, centarX, centarY,r)):
            crash(nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty)
        if(sudarKrugI4tacke(c,c+30,c,c+30,d,d,d+30,d+30, centarX, centarY,r)):
            crash(nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty)
        if(sudarKrugI4tacke(e,e+30,e,e+30,f,f,f+30,f+30, centarX, centarY,r)):
            crash(nivo, kad, x, y , a, b, c, d, e, f, thing_startx, thing_starty)

        pygame.display.update()
        clock.tick(60)

        if(score == kad):
            return (x,y,a,b,c,d,e,f,thing_startx, thing_starty)

    
game_intro()
game_loop()
pygame.quit()
quit()
