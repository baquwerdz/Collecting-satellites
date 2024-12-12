from random import randint
import pgzrun
import time

WIDTH = 800
HEIGHT = 500

satelites = []
lines = []
startTime = 0
totalTime = 0
endTime = 0
nextSatelite = 0
numberOfSatelites = 8

def createSatelite():
    for i in range (0,numberOfSatelites):
        sl = Actor("satelite")
        sl.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satelites.append(sl)

def draw():
    screen.blit("bgspace",(0,0))
    number = 1
    for  i in satelites:
        screen.draw.text(str(number),i.pos[0],i.pos[1]+20)
        i.draw()
        number = number + 1
    for i in lines:
        screen.draw.line(i[0],i[1],(255,255,255))

def on_mouse_down(pos):
    global score
    if createSatelite() 


createSatelite()


pgzrun.go()