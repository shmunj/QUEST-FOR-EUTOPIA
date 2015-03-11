import pygame, sys
from pygame import *

pygame.font.init()

def menu(screen,cursor,clock,TICK):
    pygame.mixer.music.load('snd/freefall.mod')
    pygame.mixer.music.play(-1,0.0)
    
    flag = pygame.image.load('img/flag.png')
    flag_rect = flag.get_rect()
    flag_rect.centerx = screen.get_rect().centerx
    flag_rect.y = 80

    font1 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',40)
    font2 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',30)
    font3 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',24)
    font4 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',12)
    
    title = font1.render('quest for eutopia',1,(180,20,20))
    title_rect = title.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.y = 30

    start = font2.render('start game',1,(180,20,20))
    start_selected = font2.render('start game',1,(255,255,102))
    start_rect = start.get_rect()
    start_rect.centerx = screen.get_rect().centerx
    start_rect.y = 170
    
    instructions = font2.render('instructions',1,(180,20,20))
    instructions_selected = font2.render('instructions',1,(255,255,102))
    instructions_rect = instructions.get_rect()
    instructions_rect.centerx = screen.get_rect().centerx
    instructions_rect.y = 230
    
    credits = font2.render('credits',1,(180,20,20))
    credits_selected = font2.render('credits',1,(255,255,102))
    credits_rect = credits.get_rect()
    credits_rect.centerx = screen.get_rect().centerx
    credits_rect.y = 290
    
    exit = font2.render('exit',1,(180,20,20))
    exit_selected = font2.render('exit',1,(255,255,102))
    exit_rect = exit.get_rect()
    exit_rect.centerx = screen.get_rect().centerx
    exit_rect.y = 350
    
    instructions_title = font1.render('instructions',1,(180,20,20))
    instructions_title_rect = instructions_title.get_rect()
    instructions_title_rect.centerx = screen.get_rect().centerx
    instructions_title_rect.y = 170

    instructions_back = font2.render('back',1,(180,20,20))
    instructions_back_selected = font2.render('back',1,(255,255,102))
    instructions_back_rect = instructions_back.get_rect()
    instructions_back_rect.centerx = screen.get_rect().centerx
    instructions_back_rect.y = 530
    
    credits_title = font1.render('credits',1,(180,20,20))
    credits_title_rect = credits_title.get_rect()
    credits_title_rect.centerx = screen.get_rect().centerx
    credits_title_rect.y = 170
    
    credits_back = font2.render('back',1,(180,20,20))
    credits_back_selected = font2.render('back',1,(255,255,102))
    credits_back_rect = credits_back.get_rect()
    credits_back_rect.centerx = screen.get_rect().centerx
    credits_back_rect.y = 530

    menu_instructions = [[start,start_rect,start_selected],[instructions,instructions_rect,instructions_selected],[credits,credits_rect,credits_selected],[exit,exit_rect,exit_selected]]
    selected = None
    instructions_instructions =[[instructions_back,instructions_back_rect,instructions_back_selected]]
    credits_instructions =[[credits_back,credits_back_rect,credits_back_selected]]

    songs = font2.render('music by:',1,(180,20,20))
    songs_rect = songs.get_rect()
    songs_rect.centerx = screen.get_rect().centerx
    songs_rect.y = 220
    
    purple_motion = font3.render('purple motion',1,(180,20,20))
    purple_motion_rect = purple_motion.get_rect()
    purple_motion_rect.centerx = screen.get_rect().centerx
    purple_motion_rect.y = 260
    
    baroque = font3.render('baroque',1,(180,20,20))
    baroque_rect = baroque.get_rect()
    baroque_rect.centerx = screen.get_rect().centerx
    baroque_rect.y = 290
    
    rapture = font3.render('rapture',1,(180,20,20))
    rapture_rect = rapture.get_rect()
    rapture_rect.centerx = screen.get_rect().centerx
    rapture_rect.y = 320
    
    art = font2.render('art:',1,(180,20,20))
    art_rect = art.get_rect()
    art_rect.centerx = screen.get_rect().centerx
    art_rect.y = 360

    duxel = font3.render('reanimator',1,(180,20,20))
    duxel_rect = duxel.get_rect()
    duxel_rect.centerx = screen.get_rect().centerx
    duxel_rect.y = 400
    
    code = font2.render('code:',1,(180,20,20))
    code_rect = code.get_rect()
    code_rect.centerx = screen.get_rect().centerx
    code_rect.y = 440

    bora_cola = font3.render('shmunj',1,(180,20,20))
    bora_cola_rect = bora_cola.get_rect()
    bora_cola_rect.centerx = screen.get_rect().centerx
    bora_cola_rect.y = 480

    credits_list = [[songs,songs_rect],[purple_motion,purple_motion_rect],[baroque,baroque_rect],[rapture,rapture_rect],[art,art_rect],[duxel,duxel_rect],[code,code_rect],[bora_cola,bora_cola_rect]]
    
    #instructions
    ministers = range(6)
    eubuttons = ['img/eumeter/pay-off.png','img/eumeter/pay-on.png']
    minister = pygame.image.load('img/minister/minister%s.png' % ministers[0])
    eubutton = pygame.image.load(eubuttons[0])
    building1 = pygame.image.load('img/objects/%s/0.png' % ministers[0])
    building2 = pygame.image.load('img/objects/%s/1.png' % ministers[0])
    building3 = pygame.image.load('img/objects/%s/2.png' % ministers[0])
    instructions_ministers = font4.render('bribe your ministers in order to sell their buildings',1,(180,20,20))
    instructions_ministers_rect = instructions_ministers.get_rect()
    instructions_ministers_rect.x = 50
    instructions_ministers_rect.y = 260
    instructions_eubutton = font4.render('pay your debt by clicking the blue button',1,(180,20,20))
    instructions_eubutton_rect = instructions_eubutton.get_rect()
    instructions_eubutton_rect.x = 50
    instructions_eubutton_rect.y = 460
    
    menu_option = 'mainmenu'
    
    t = 0
    while 1:
        clock.tick(TICK)
        t += 1
        mx,my = pygame.mouse.get_pos()

        screen.fill((0,0,0))
        screen.blit(title,title_rect)
        screen.blit(flag,flag_rect)
            
        
        #current menu
        if menu_option == 'mainmenu':
            #mouse hover/select
            if mx in range(start_rect.x,start_rect.x + start_rect.width) and my in range(start_rect.y,start_rect.y + start_rect.height):
                selected = start
            elif mx in range(instructions_rect.x,instructions_rect.x + instructions_rect.width) and my in range(instructions_rect.y,instructions_rect.y + instructions_rect.height):
                selected = instructions
            elif mx in range(credits_rect.x,credits_rect.x + credits_rect.width) and my in range(credits_rect.y,credits_rect.y + credits_rect.height):
                selected = credits
            elif mx in range(exit_rect.x,exit_rect.x + exit_rect.width) and my in range(exit_rect.y,exit_rect.y + exit_rect.height):
                selected = exit

            else:
                selected = None

            for i in menu_instructions:
                if selected == i[0]:
                    screen.blit(i[2],i[1])
                else:
                    screen.blit(i[0],i[1])
        
        elif menu_option == 'instructions': #change
            screen.blit(instructions_title,instructions_title_rect)
           
            if t % 40 == 0:
                ministers = ministers[-1:] + ministers[:-1]
                eubuttons = eubuttons[-1:] + eubuttons[:-1]
                minister = pygame.image.load('img/minister/minister%s.png' % ministers[0])
                building1 = pygame.image.load('img/objects/%s/0.png' % ministers[0])
                building2 = pygame.image.load('img/objects/%s/1.png' % ministers[0])
                building3 = pygame.image.load('img/objects/%s/2.png' % ministers[0])
                eubutton = pygame.image.load(eubuttons[0])

            screen.blit(instructions_ministers,instructions_ministers_rect)
            screen.blit(instructions_eubutton,instructions_eubutton_rect)
            screen.blit(minister,(50,300))
            screen.blit(building1,(190,310))
            screen.blit(building2,(230,310))
            screen.blit(building3,(270,310))
            screen.blit(eubutton,(350,400))
            screen.fill((104,49,49),(150,370,34,20))
            screen.fill((174,138,99),(190,370,34,20))
            screen.fill((196,202,131),(230,370,34,20))
            screen.fill((78,144,94),(270,370,34,20))

            #mouse hover/select
            if mx in range(instructions_back_rect.x,instructions_back_rect.x + instructions_back_rect.width) and my in range(instructions_back_rect.y,instructions_back_rect.y + instructions_back_rect.height):
                selected = instructions_back
            else:
                selected = None
            
            for i in instructions_instructions:
                if selected == i[0]:
                    screen.blit(i[2],i[1])
                else:
                    screen.blit(i[0],i[1])
        
        elif menu_option == 'credits': #change
            screen.blit(credits_title,credits_title_rect)
            
            #mouse hover/select
            if mx in range(credits_back_rect.x,credits_back_rect.x + credits_back_rect.width) and my in range(credits_back_rect.y,credits_back_rect.y + credits_back_rect.height):
                selected = credits_back
            else:
                selected = None
            
            for i in credits_instructions:
                if selected == i[0]:
                    screen.blit(i[2],i[1])
                else:
                    screen.blit(i[0],i[1])
            
            #credits
            for c in credits_list:
                screen.blit(c[0],c[1])
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                if menu_option == 'mainmenu':
                    pygame.quit()
                    sys.exit()
                else:
                    menu_option = 'mainmenu'

            elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if selected == start:
                    return
                elif selected == instructions:
                    menu_option = 'instructions'
                elif selected == credits:
                    menu_option = 'credits'
                elif selected == exit:
                    pygame.quit()
                    sys.exit()
                elif selected == instructions_back or selected == credits_back:
                    menu_option = 'mainmenu'
                else:
                    pass
        
        screen.blit(cursor.img,(mx,my))
        
        pygame.display.flip()

