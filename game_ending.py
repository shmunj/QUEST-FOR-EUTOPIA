import pygame, sys
from pygame import *
from random import randint

pygame.font.init()

def message(outcome,score,screen,cursor,clock,TICK): #za sada samo
    if outcome == 'good':
        msg = 'you did it!'
        clr = (255,255,102)
    elif outcome == 'bad':
        msg = 'you failed...'
        clr = (180,20,20)
    
    pygame.mixer.music.load('snd/freefall.mod')
    pygame.mixer.music.play(-1,0.0)
    
    font1 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',40)
    font2 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',30)
    font3 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',20)
    
    gameover = font1.render('game over',1,(180,20,20))
    gameover_rect = gameover.get_rect()
    gameover_rect.centerx = screen.get_rect().centerx
    gameover_rect.y = 30

    outcome_msg = font2.render(msg,1,clr)
    outcome_msg_rect = outcome_msg.get_rect()
    outcome_msg_rect.centerx = screen.get_rect().centerx
    outcome_msg_rect.y = 170

    see_results = font2.render('see your score',1,(108,20,20))
    see_results2 = font2.render('see your score',1,(255,255,102))
    see_results_rect = see_results.get_rect()
    see_results_rect.centerx = screen.get_rect().centerx
    see_results_rect.y = 400
    
    show_results = False
    while show_results == False:
        clock.tick(TICK)
        mx,my = pygame.mouse.get_pos()

        screen.fill((0,0,0)) #slika
        screen.blit(gameover,gameover_rect)
        screen.blit(outcome_msg,outcome_msg_rect)
        
        #mouse hover
        if mx in range(see_results_rect.x,see_results_rect.x + see_results_rect.width) and my in range(see_results_rect.y,see_results_rect.y + see_results_rect.height):
            selected = 'results'
        else:
            selected = None

        if selected == 'results':
            screen.blit(see_results,see_results_rect)
        else:
            screen.blit(see_results2,see_results_rect)

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if selected == 'results':
                    show_results = True

        screen.blit(cursor.img,(mx,my))
        pygame.display.flip()

    score_lines = {0:[None,[[None,None],[None,None],[None,None]]],
    1:[None,[[None,None],[None,None],[None,None]]],
    2:[None,[[None,None],[None,None],[None,None]]],
    3:[None,[[None,None],[None,None],[None,None]]],
    4:[None,[[None,None],[None,None],[None,None]]],
    5:[None,[[None,None],[None,None],[None,None]]]}
    for so in score.objects:
        score_lines[so][0] = pygame.Surface((screen.get_width(),44))
    for line in score_lines:
        for obj in range(0,3):
            score_lines[line][1][obj][0] = font3.render(str(score.objects[line][obj]) + 'x',1,(255,255,102))
            score_lines[line][1][obj][1] = pygame.image.load('img/objects/%s/%s.png' % (line,obj))
    
    while 1:
        clock.tick(TICK)
        mx,my = pygame.mouse.get_pos()
       
        screen.fill((0,0,0))
       
        y = 50
        for line in score_lines:
            x = 0
            for obj in range(0,3):
                x += 150
                score_lines[line][0].blit(score_lines[line][1][obj][0],(x,0))
                score_lines[line][0].blit(score_lines[line][1][obj][1],(x+50,0))
                screen.blit(score_lines[line][0],(0,y))
            y += 50

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        screen.blit(cursor.img,(mx,my))
        
        pygame.display.flip()

def eunization(screen,clock,TICK):
    beep = pygame.mixer.Sound('snd/tick.wav')

    map_img = pygame.image.load('img/map/map.png')
    borders_img = pygame.image.load('img/map/borders.png')#granica slika
    blue_borders = [pygame.image.load('img/map/eu_spreading/0.png'),pygame.image.load('img/map/eu_spreading/1.png'),pygame.image.load('img/map/eu_spreading/2.png'),pygame.image.load('img/map/eu_spreading/3.png')]
    spreading_order = 0
    converted_land = pygame.Surface((map_img.get_width(),map_img.get_height()),pygame.SRCALPHA,32)
    converted_land = converted_land.convert_alpha()
    blue_color = (31,66,167)
    blue_w = map_img.get_width()
    blue_h = 0
    
    t = 0
    while blue_h <= 600:
        clock.tick(TICK)
        t += 1
        
        if t % 2 == 0:
            screen.blit(map_img,(90,0))
            blue_h += 6
            converted_land.fill(blue_color,(0,0,blue_w,blue_h))
            spr_w = 0
            blue_borders = blue_borders[-1:] + blue_borders[:-1]
            for i in range(2):
                for spr in blue_borders:
                    converted_land.blit(spr,(spr_w,blue_h))
                    spr_w += 88
            screen.blit(converted_land,(90,0))
            screen.blit(borders_img,(90,0))
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
                #pygame.quit()
                #sys.exit()
        
        pygame.display.flip()

    shadow = pygame.Surface((map_img.get_width(),map_img.get_height()),pygame.SRCALPHA,32)
    shadow = shadow.convert_alpha()

    shadow_border_img = pygame.image.load('img/map/shadow-border.png')
    shadow_border_img.convert_alpha()

    shadow_w = blue_w
    shadow_h = 0 - shadow_border_img.get_height()
    
    cover_img = pygame.image.load('img/map/cover.png')
    cover_x = -292 #-292
    cover_y = -1550 #-216

    t = 0
    while cover_y < 0:
        clock.tick(TICK)
        t += 1
        
        if t % (TICK*2) == 0:
            beep.play()

        if t % 8 == 0 and cover_y >= -1216:
            cover_x += 2
        
        if t % 2 == 0:
            shadow_h += 2
            cover_y += 3
            screen.blit(converted_land,(90,0))
            shadow.fill((0,0,0,60),(0,0,shadow_w,shadow_h))
            screen.blit(borders_img,(90,0))
            screen.blit(shadow,(90,0))
            screen.blit(shadow_border_img,(0,shadow_h))
            screen.blit(cover_img,(90+cover_x,cover_y))
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
                #pygame.quit()
                #sys.exit()
        
        pygame.display.flip()

    separation(True,screen,clock,TICK)

def separation(game_won,screen,clock,TICK):
    pygame.mixer.music.load('snd/rapture_-_lost_in_space.mod')
    pygame.mixer.music.play(-1,0.0)
    
    europe = pygame.image.load('img/map/europe.png')
    serbia = pygame.image.load('img/map/serbia.png')
    
    fire_s0 = pygame.image.load('img/fx/fire s 0.png')
    fire_s1 = pygame.image.load('img/fx/fire s 1.png')
    fire_b0 = pygame.image.load('img/fx/fire b 0.png')
    fire_b1 = pygame.image.load('img/fx/fire b 1.png')
    
    fire1 = [fire_s0, fire_s1]
    fire2 = [fire_b0, fire_b1]
    fire = fire2

    if game_won:
        eutopia = pygame.image.load('img/map/eutopia.png')
    else:
        eutopia = pygame.image.load('img/map/eutopia-s.png')
    
    eutopia_y = 0
    shake = 2

    t = 0
    while eutopia_y > -280:
        clock.tick(TICK)
        t += 1
        
        screen.fill((0,0,0))
        screen.blit(europe,(0,0))
        if not game_won:
            screen.blit(serbia,(0,0))
        
        if t <= 100: #still
            if t % 6 == 0:
                pass
        
        elif t <= 150: #shaking animation - slow
            if t % 6 == 0:
                shake = shake * (-1)
                eutopia_y += shake
        elif t > 150 and t <= 185: #shaking animation - faster
            if t % 3 == 0:
                shake = shake * (-1)
                eutopia_y += shake
        
        else:
            if t % 4 == 0 and eutopia_y > -50: #slow movement at first
                eutopia_y -= 1
                fire = fire1
            if t % 4 == 0 and eutopia_y > -150 and eutopia_y <= -50: #slow movement 2
                eutopia_y -= 1
                fire = fire2
            elif t % 4 == 0 and eutopia_y <= -150: #faster animation
                eutopia_y -= 2
                fire = fire1
            
            fire = fire[-1:] + fire[:-1]
            screen.blit(fire[0],(0,eutopia_y))
        
        screen.blit(eutopia,(0,eutopia_y))
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
                #pygame.quit()
                #sys.exit()
        
        pygame.display.flip()

    space_scene(game_won,screen,clock,TICK)

class Star:
    def __init__(self,x,y,blink_time,TICK):
        self.x = x
        self.y = y
        self.blink_time = blink_time * TICK + randint(0,TICK)
        self.blinking = False
        self.shine = 3
        self.blink = 2
        self.size = self.shine
        self.blink_frame = TICK / 2

def space_scene(game_won,screen,clock,TICK):
    if game_won:
        eutopia = pygame.image.load('img/map/eutopia.png')
    else:
        eutopia = pygame.image.load('img/map/eutopia-s.png')

    eutopia_x,eutopia_y = (250,245)

    earth = pygame.image.load('img/space/earth.png') 
    earth_x,earth_y = (131,175)

    moon = pygame.image.load('img/space/moon.png')
    moon_x,moon_y = (426,379)
    
    mars = pygame.image.load('img/space/mars.png')
    mars_x,mars_y = (800,200)
    sun = pygame.image.load('img/space/sun.png')
    sun_x,sun_y = (800,16)

    stars = [Star(140,58,randint(3,6),TICK),Star(111,130,randint(3,6),TICK),Star(80,245,randint(3,6),TICK),Star(264,110,randint(3,6),TICK),Star(342,80,randint(3,6),TICK),Star(4,380,randint(3,6),TICK),Star(138,412,randint(3,6),TICK),Star(40,522,randint(3,6),TICK),Star(242,495,randint(3,6),TICK),Star(360,468,randint(3,6),TICK),Star(540,586,randint(3,6),TICK),Star(750,500,randint(3,6),TICK),Star(782,453,randint(3,6),TICK),Star(595,350,randint(3,6),TICK),Star(507,166,randint(3,6),TICK),Star(606,23,randint(3,6),TICK),Star(758,72,randint(3,6),TICK)]

    
    eutopia_w,eutopia_h = (60,80)

    t = 0
    while (eutopia_x,eutopia_y) < (432,175):
        clock.tick(TICK)
        t += 1

        for star in stars:
            if t % star.blink_time == 0:
                star.blinking = True

            if star.blinking == True:
                star.size = star.blink
                star.blink_frame -= 1
            
                if star.blink_frame <= 0:
                    star.blinking = False
                    star.blink_frame = 40
            else:
                star.size = star.shine

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
                #pygame.quit()
                #sys.exit()
                   
        screen.fill((0,0,0))
        for star in stars:
            screen.fill((255,255,255),(star.x,star.y,star.size,star.size))
       
        screen.blit(earth,(earth_x,earth_y))
        
        if t % TICK == 0:
            moon_x -= 1

        screen.blit(moon,(moon_x,moon_y))

        if t <= TICK * 2:
            if t % 4 == 0:
                eutopia_h += 2
                eutopia_x += 1
            if t % 3 == 0:
                eutopia_w += 2
        elif t > TICK *2:
            if t % 4 == 0:
                eutopia_h += 2
                eutopia_x += 2
            if t % 3 == 0:
                eutopia_w += 2
                eutopia_y -= 1
            
        
        screen.blit(pygame.transform.scale(eutopia,(eutopia_w,eutopia_h)),(eutopia_x,eutopia_y))
        
        pygame.display.flip()

    t = 0
    while sun_x >= 579:
        clock.tick(TICK)
        t += 1

        screen.fill((0,0,0))

        for star in stars:
            if t % star.blink_time == 0:
                star.blinking = True

            if star.blinking == True:
                star.size = star.blink
                star.blink_frame -= 1
            
                if star.blink_frame <= 0:
                    star.blinking = False
                    star.blink_frame = 40
            else:
                star.size = star.shine
        
        if t % TICK == 0:
            moon_x -= 1
        
        if t % 2 == 0:
            for star in stars:
                star.x -= 1
        
            earth_x -= 2
            moon_x -= 2
            eutopia_x -= 1
        
        for star in stars:
            screen.fill((255,255,255),(star.x,star.y,star.size,star.size))
       
        screen.blit(earth,(earth_x,earth_y))
        screen.blit(moon,(moon_x,moon_y))
        screen.blit(pygame.transform.scale(eutopia,(eutopia_w,eutopia_h)),(eutopia_x,eutopia_y))
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
                #pygame.quit()
                #sys.exit()

        if moon_x <= 50:
            if t % 2 == 0:
                mars_x -= 1
            screen.blit(mars,(mars_x,mars_y))
        if moon_x <= -150:
            if t % 2 == 0:
                sun_x -= 1
            screen.blit(sun,(sun_x,sun_y))

        pygame.display.flip()
