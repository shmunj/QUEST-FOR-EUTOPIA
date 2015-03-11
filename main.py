#!/usr/bin/python
import pygame
from random import randint
from pygame import *
import sys

#GAME CLASSES
import intro
import mainmenu
from minister import Minister
from game_map import Map
from nodes import Node
from nodes import Building
import eumeter
from cursor import Cursor
import game_ending
#----------------------------

pygame.init()
game_over = False

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Quest for EUtopia')
fullscreen = False

clock = pygame.time.Clock()
t = 0
sec = 0
TICK = 40
TOCK = TICK/3

mx = 900
my = 700
selected = None

#cursor
pygame.mouse.set_visible(0)
cursor = Cursor()
cursor.normal()

#game intro
intro.play(screen,clock,TICK)

#main menu
mainmenu.menu(screen,cursor,clock,TICK)

################  GAME  ######################
#game objects
gamemap = Map(90,0)

game_time = 180
progress = eumeter.Progress(0,30000,game_time) #iz cfg fajla - options
score = eumeter.Score()
bar = eumeter.Bar(screen)
displays = eumeter.Displays(screen)
kosovo_display = eumeter.Kosovo_display(displays.x)
paybutton = eumeter.Paybutton(screen)
#LAMP

ministers = {0:Minister(0,0,0),1:Minister(1,0,100),2:Minister(2,0,200),3:Minister(3,0,300),4:Minister(4,0,400),5:Minister(5,0,500)}

nodes = {}
nodes_all = open('nodes','r').read().split('\n')
nodes_all.pop()
for node in nodes_all:
    nxy = node.split(',')
    nodes[nodes_all.index(node)] = Node((int(nxy[0]),int(nxy[1])))

buildings = {}
for node in nodes:
    buildings[node] = Building(randint(0,5),nodes[node],node)
    nodes[node].wait = 6
can_sell = False

#music
pygame.mixer.music.load('snd/CCITY12.S3M')
pygame.mixer.music.play(-1,0.0)

tick = pygame.mixer.Sound('snd/t.wav')
sellsound = pygame.mixer.Sound('snd/sell.wav')
cantsellsound = pygame.mixer.Sound('snd/cantsell.wav')
yesss = pygame.mixer.Sound('snd/yesss.wav')

while game_over == False:
    #clock
    clock.tick(TICK)
    t += 1
    
    if t % TICK == 0:
        if progress.payup >= progress.goal:
            game_over = True

        #check progress
        if progress.time > 0:
            progress.time -= 1
        
            #check when was the last payment made
            if progress.time - progress.last_payment > 30:
                progress.goal += 1000
            
            completed = (game_time - progress.time) * 100 / game_time
            if completed == 25:
                if progress.get_progress() < completed:
                    progress.goal += 1000
            elif completed == 50:
                if progress.get_progress() < completed:
                    progress.goal += 1000
            elif completed == 75:
                if progress.get_progress() < completed:
                    progress.goal += 1000

        else:
            game_over = True

        #check kosovo
        if gamemap.kosovo_sold == True:
            if gamemap.kosovo_timeout > 0:
                gamemap.kosovo_timeout -= 1
            else:
                gamemap.kosovo_sold = False
                gamemap.kosovo_timeout = 30
                gamemap.img = gamemap.img_with_kosovo

    if t % TOCK == 0:
        tick.play()

    #blank screen
    screen.fill((0,0,0))
    
    #draw map
    screen.blit(gamemap.img,(gamemap.x,gamemap.y))
    if gamemap.kosovo_sold == True:
        screen.blit(gamemap.kosovo_counter(t)[0],gamemap.kosovo_counter(t)[1])

    #draw nodes
    for building in buildings:
        if buildings[building] != None:
            screen.blit(buildings[building].img,(ministers[0].img.get_width() + ministers[0].scroll_img.get_width() + buildings[building].node.position[0],buildings[building].node.position[1] + gamemap.y))
    
    if t % TICK == 0:
        for building in buildings.keys():
            if buildings[building] != None:
                buildings[building].checkGrowth()
    
        #check for empty nodes
        for node in nodes:
            if nodes[node].building == None:
                if nodes[node].wait <= 10:
                    nodes[node].wait += 1
                else:
                    if randint(0,20) == 20:
                        #chance to spawn a special building
                        if randint(0,20) == 20:
                            buildings[node] = Building(6,nodes[node],node)
                        else:
                            buildings[node] = Building(randint(0,5),nodes[node],node)
                
    #draw interface
    ####ministers
    for key in ministers.keys():
        if t % TICK == 0:
            sec += 1
            ministers[key].checkCost()
        if ministers[key].animate_scroll != 0:
            if ministers[key].animateScroll() != False:
                screen.blit(ministers[key].bill,(ministers[key].bill_pos,ministers[key].y))
        screen.blit(ministers[key].scroll(),(ministers[key].x + ministers[key].img.get_width(),ministers[key].y))
        screen.blit(ministers[key].img,(ministers[key].x,ministers[key].y))
    
    ####displays
    ########kosovo display
    if gamemap.kosovo_sold == True:
        screen.blit(kosovo_display.draw(),(kosovo_display.x,kosovo_display.y))
    ########the rest
    screen.blit(displays.draw(progress.money,progress.time,t),(displays.x,displays.y))
    
    ####bar
    screen.blit(bar.draw(progress.get_progress()),(bar.x,bar.y))
    
    ####paybutton
    screen.blit(paybutton.draw(),(paybutton.x,paybutton.y))
    
    #cursor position
    mx,my = pygame.mouse.get_pos()

    #cursor hover
    ####over ministers
    if mx <= ministers[0].img.get_width() + ministers[0].scroll_img.get_width():
        for key in ministers.keys():
            if my in range(ministers[key].y,ministers[key].y+100):
                if ministers[key].animate_scroll != 1:
                    ministers[key].animate_scroll = 1
                if mx <= ministers[0].img.get_width():
                    selected = ministers[key]
                    screen.blit(selected.bribe_img,(selected.x,selected.y))
    
    ####over paybutton
    elif mx in range(paybutton.x,paybutton.x+92) and my in range(paybutton.y,paybutton.y+51):
        selected = 'paybutton'

    ####over map
    else:
        selected = None

        for key in ministers.keys():
            if ministers[key].animate_scroll != 0:
                ministers[key].animate_scroll = -1

        for building in buildings:
            if buildings[building] != None and mx - ministers[0].img.get_width() - ministers[0].scroll_img.get_width() in range(buildings[building].node.position[0],buildings[building].node.position[0] + 34) and my in range(buildings[building].node.position[1] + gamemap.y ,buildings[building].node.position[1] + 44 + gamemap.y) and buildings[building].object_type != None:
                selected = buildings[building]
                
                if buildings[building].object_type < 6:
                    if buildings[building].level <= 2 - ministers[buildings[building].object_type].restriction and ministers[buildings[building].object_type].restriction != 3:
                        can_sell = True
                        cursor.sell()
                    else:
                        can_sell = False
                        cursor.cant_sell()
                else:
                    can_sell = True
                    cursor.sell()

        #over Kosovo
        if (mx in range(90+301,90+379) and my in range(693+gamemap.y,729+gamemap.y)) or (mx in range(90+273,90+399) and my in range(729+gamemap.y,761+gamemap.y)) or (mx in range(90+241,90+419) and my in range(761+gamemap.y,871+gamemap.y)): #ima jos
            if gamemap.kosovo_sold == False:
                selected = 'kosovo'
                screen.blit(gamemap.kosovo_sell_img,gamemap.get_kosovo_pos())

    #draw cursor
    if isinstance(selected,Building):#za sada
        screen.blit(cursor.img,(mx-(cursor.img.get_width()/2),my-(cursor.img.get_width()/2)))

    else:
        cursor.normal()
        screen.blit(cursor.img,(mx,my))

    #events
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_f:
            if fullscreen == False:
                screen = pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                fullscreen = True
            else:
                screen = pygame.display.set_mode((800,600))
                fullscreen = False

        #map navigation
        elif event.type == MOUSEBUTTONDOWN and event.button == 5:
            if gamemap.y - 50 < screen.get_height() - gamemap.height:
                gamemap.y = screen.get_height() - gamemap.height
            else:
                gamemap.y -= 50
        elif event.type == MOUSEBUTTONDOWN and event.button == 4:
            if gamemap.y + 50 > 0:
                gamemap.y = 0
            else:
                gamemap.y += 50

        #mouse click
        elif event.type == MOUSEBUTTONDOWN and selected == 'paybutton':
            paybutton.pressed = True
        
        elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if isinstance(selected,Building):
                if can_sell == True:
                    selected.sell(True,progress,score)
                    if selected.object_type >= 6:
                        selected.special()
                    buildings[selected.key] = None
                    nodes[selected.key].building = None
                    sellsound.play()
                else:
                    selected.sell(False,progress,score)
                    cantsellsound.play()

            elif isinstance(selected,Minister):
                if progress.money >= selected.cost:
                    selected.bribe(progress)
                    sellsound.play()
                else:
                    cantsellsound.play()

            elif selected == 'kosovo':
                gamemap.img = gamemap.img_without_kosovo
                gamemap.kosovo_sold = True
                progress.money += 5000
                yesss.play()

            else:
                pass
        
        elif event.type == MOUSEBUTTONUP and paybutton.pressed == True:
            if selected == 'paybutton':
                if progress.money <= 0:
                    #zvuk
                    print "NOPE"
                elif progress.money >= 500:
                    progress.last_payment = progress.time
                    progress.money -= 500
                    progress.payup += 500
                else:
                    progress.last_payment = progress.time
                    progress.money -= progress.money
                    progress.payup -= progress.money
            paybutton.pressed = False
    
    pygame.display.flip()

############## game over ##############
cursor.normal()

pygame.mixer.music.stop()

if progress.time <= 0:
    outcome = 'bad'
    game_ending.separation(False,screen,clock,TICK) #test samo
else:
    outcome = 'good'
    game_ending.eunization(screen,clock,TICK)

game_ending.message(outcome,score,screen,cursor,clock,TICK)
