#!/usr/bin/python
import pygame,datetime
from pygame import *

def play(screen,clock,TICK):
    pygame.mixer.music.load('snd/2ND_PM.S3M')
    pygame.mixer.music.play(-1,0.0)

    song_time = [1000,8000,11500,15000,19000,22500,26000,30000,33750,41000,44850,52000,60000,63000,78300]

    scene = [scene0,scene1,scene2,scene3,scene4,scene5,scene6,scene7,scene8,scene9,scene10,scene11,scene12,scene13]
    text = {
    0:'in the near future',
    1:'the world falls prey \nto a financial crisis',
    2:'caused by rapid depletion \nof natural resources',
    3:'and transforming the earth \ninto an uninhabitable place...',
    4:'the old ideologies arose again',
    5:'as the answer to the collapse of america,\nthe leading capitalist power of the past...',
    6:'the european union as the only\nfinancially stable political power',
    7:'started working on the project\nunder the code name eutopia',
    8:'a plan that is supposed to turn\nthe whole eu into a spaceship',
    9:'and send it on the mission\nof colonization of mars',
    10:'will any of the new third world\ncountries repay their debts',
    11:'and meet the requirements for filling\nthe last place in the spaceship eutopia...',
    12:'',
    13:'...until launch?'
    }
    
    font = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',20)

    flip = False
    dot_speed = 50
    dot_color = (180,20,20)
    dot_w = 80
    dot_h = 6
    dot1_x = 0 - dot_w
    dot1_y = 102
    dot1_direction = -1
    dot2_x = screen.get_width()
    dot2_y = 400 - dot_h
    dot2_direction = 1

    logo = pygame.image.load('img/logo.png')

    ml = False
    st = -1
    t = 0
    
    fullscreen = False
    
    while 1:
        clock.tick(TICK)
        t += 1

        screen.blit(logo,(0,102))

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_f:
                if fullscreen == False:
                    screen = pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                    fullscreen = True
                else:
                    screen = pygame.display.set_mode((800,600))
                    fullscreen = False

        #slike
        if st != -1:
            if st == 12 or st == 13:
                current_scene.change(t,TICK)
                current_scene.draw(screen)
            else:
                current_scene.change(t)
                current_scene.draw(screen)

        screen.fill((0,0,0),(0,0,800,102))
        screen.fill((0,0,0),(0,400,800,200))

        if pygame.mixer.music.get_pos() >= song_time[st+1]:
            st += 1
            if st == 14:
                return
            elif st > 0:
                previous_scene = current_scene
                current_scene = scene[st](screen,previous_scene)
            else:
                current_scene = scene[st](screen)

            flip = True
            dot1_direction = dot1_direction * (-1)
            dot2_direction = dot2_direction * (-1)

            if st == 14:
                return

            elif '\n' in text[st]:
                ml = True
                txt = text[st].split('\n')
                txt1 = txt[0]
                txt2 = txt[1]
                
                subtitle1 = font.render(txt1,1,(180,20,20))
                subtitle1_rect = subtitle1.get_rect()
                subtitle1_rect.centerx = screen.get_rect().centerx
                subtitle1_rect.y = 430
                
                subtitle2 = font.render(txt2,1,(180,20,20))
                subtitle2_rect = subtitle2.get_rect()
                subtitle2_rect.centerx = screen.get_rect().centerx
                subtitle2_rect.y = 460
            
            else:
                ml = False
                subtitle = font.render(text[st],1,(180,20,20))
                subtitle_rect = subtitle.get_rect()
                subtitle_rect.centerx = screen.get_rect().centerx
                subtitle_rect.y = 430
        
        if flip:
            dot1_x += dot1_direction * dot_speed
            dot2_x += dot2_direction * dot_speed
            if dot1_direction > 0 and dot1_x > screen.get_width():
                dot1_x = screen.get_width()
                dot2_x = 0 - dot_w
                flip = False
            elif dot1_direction < 0 and dot1_x < 0:
                dot2_x = screen.get_width()
                dot1_x = 0 - dot_w
                flip = False

        screen.fill(dot_color,(dot1_x,dot1_y,dot_w,dot_h))
        screen.fill(dot_color,(dot2_x,dot2_y,dot_w,dot_h))
        
        if st != -1 and not ml:
            screen.blit(subtitle,subtitle_rect)
        elif st != -1 and ml:
            screen.blit(subtitle1,subtitle1_rect)
            screen.blit(subtitle2,subtitle2_rect)
            
        pygame.display.flip()

class scene0:
    def __init__(self,screen):
        self.movie_layer = pygame.Surface((screen.get_width(),screen.get_height()))
        
        self.earth = pygame.image.load('img/space/earth normal.png')
        self.earth_dimensions = (432,410)
        self.earth_x = 47
        self.earth_y = 47

        self.moon = pygame.image.load('img/space/moon.png')
        self.moon_x = 569
        self.moon_y = 187
    
    def draw(self,screen):
        self.movie_layer.fill((0,0,0))
        self.movie_layer.blit(self.moon,(self.moon_x,self.moon_y))
        self.movie_layer.blit(pygame.transform.scale(self.earth,(self.earth_dimensions)),(self.earth_x,self.earth_y))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        if t % 10 == 0:
            self.moon_x -= 1

class scene1:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer
        
        self.earth = previous.earth
        self.red = pygame.image.load('img/space/earth RED.png')
        self.red_opacity = 1
        self.earth_dimensions = previous.earth_dimensions
        self.earth_x = previous.earth_x
        self.earth_y = previous.earth_y

        self.moon = previous.moon
        self.moon_x = previous.moon_x
        self.moon_y = previous.moon_y
    
    def draw(self,screen):
        self.movie_layer.fill((0,0,0))
        self.movie_layer.blit(self.moon,(self.moon_x,self.moon_y))
        self.movie_layer.blit(pygame.transform.scale(self.earth,(self.earth_dimensions)),(self.earth_x,self.earth_y))
        for i in range(self.red_opacity):
            self.movie_layer.blit(pygame.transform.scale(self.red,(self.earth_dimensions)),(self.earth_x,self.earth_y))
        
        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        if t % 4 == 0:
            self.moon_x -= 1
        if t % 8 == 0:
            self.red_opacity += 1

class scene2:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.clouds1 = pygame.image.load('img/anim/clouds 1.png')
        self.clouds1_x = 54
        self.clouds2 = pygame.image.load('img/anim/clouds 2.png')
        self.clouds2_x = 166
        
        self.sun = pygame.image.load('img/anim/sun.png')
        self.platforms = pygame.image.load('img/anim/platforms.png')

        self.water_color = (2,63,138)
        self.sky1_color = (90,129,176)
        self.sky2_color = (92,106,123)
        self.dark_sky = 0

    def draw(self,screen):
        self.movie_layer.fill(self.sky1_color,(0,0,800,600))
        self.movie_layer.fill(self.sky2_color,(0,346-self.dark_sky,800,self.dark_sky))
        self.movie_layer.fill(self.water_color,(0,346,800,200))
        
        self.movie_layer.blit(self.sun,(524,120))
        self.movie_layer.blit(self.clouds1,(self.clouds1_x,102))
        self.movie_layer.blit(self.clouds2,(self.clouds2_x,204))
        
        self.movie_layer.blit(self.platforms,(0,114))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        if t % 5 == 0:
            self.clouds2_x -= 1
        if t % 3 == 0:
            if self.dark_sky < 30:
                self.dark_sky += 4
            elif self.dark_sky >= 30 and self.dark_sky < 60:
                self.dark_sky += 6
            else:
                self.dark_sky += 8
            self.clouds1_x -= 1

class scene3:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.hazmat = pygame.image.load('img/anim/hazmat.png')
        self.hazmat_x = 444
        
        self.background = pygame.image.load('img/anim/burning ocean.png')
        self.background_x = 0

        self.fire1 = pygame.image.load('img/anim/ocean fire 0.png')
        self.fire2 = pygame.image.load('img/anim/ocean fire 1.png')
        self.fires = [self.fire1,self.fire2]
        self.fire_x = 606

    def draw(self,screen):
        self.movie_layer.blit(self.background,(self.background_x,102))
        self.movie_layer.blit(self.hazmat,(self.hazmat_x,232))
        self.fire = self.fires[0]
        self.movie_layer.blit(self.fire,(self.fire_x,102))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        if t % 3 == 0:
            self.background_x -= 3
            self.fire_x -= 3
        if t % 5 == 0:
            self.hazmat_x -= 3
        if t % 8 == 0:
            self.fires = self.fires[-1:] + self.fires[:-1]

class scene4:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer
        self.timer = 0

        self.mosque = pygame.image.load('img/anim/mosque.png')
        self.mosque_x = 550
        self.mosque_y = 200
        
        self.building = pygame.image.load('img/anim/building.png')
        self.building_x = -30
        self.building_y = 200
        
        #mozda i scale za avione?
        self.airplane = pygame.image.load('img/anim/airplane.png')
        self.airplane1_x = 386
        self.airplane1_y = 400
        
        self.airplane2_x = 316
        self.airplane2_y = 510
        
        self.airplane3_x = 480
        self.airplane3_y = 510

        self.airplane_start1_x = self.movie_layer.get_width() / 2 + 50
        self.airplane_start1_y = self.movie_layer.get_height() + 300
        self.airplane_start2_x = self.movie_layer.get_width() / 2 - 50
        self.airplane_start2_y = self.movie_layer.get_height() + 300

    def draw(self,screen):
        self.movie_layer.fill((103,80,76))
        
        #trapez
        pygame.draw.polygon(self.movie_layer,(147,127,124),((self.airplane1_x + 30,self.airplane1_y + 80),(self.airplane1_x + 50,self.airplane1_y + 80),(self.airplane_start1_x, self.airplane_start1_y),(self.airplane_start2_x, self.airplane_start2_y)),0)
        pygame.draw.polygon(self.movie_layer,(147,127,124),((self.airplane2_x + 50,self.airplane2_y + 80),(self.airplane2_x + 70,self.airplane2_y + 80),(self.airplane_start1_x, self.airplane_start1_y),(self.airplane_start2_x, self.airplane_start2_y)),0)
        pygame.draw.polygon(self.movie_layer,(147,127,124),((self.airplane3_x + 30,self.airplane3_y + 80),(self.airplane3_x + 50,self.airplane3_y + 80),(self.airplane_start1_x, self.airplane_start1_y),(self.airplane_start2_x, self.airplane_start2_y)),0)
        
        self.movie_layer.blit(self.airplane,(self.airplane1_x,self.airplane1_y))
        self.movie_layer.blit(pygame.transform.rotate(self.airplane,20),(self.airplane2_x,self.airplane2_y))
        self.movie_layer.blit(pygame.transform.rotate(self.airplane,340),(self.airplane3_x,self.airplane3_y))
        
        self.movie_layer.blit(self.mosque,(self.mosque_x,self.mosque_y))
        self.movie_layer.blit(self.building,(self.building_x,self.building_y))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        self.timer += 1
       
        if t % 2 == 0:
            if self.mosque_x <= self.movie_layer.get_width() - self.mosque.get_width():
                self.mosque_x = self.movie_layer.get_width() - self.mosque.get_width()
            else:
                self.mosque_x -= 2
            
            if self.building_x >= 0:
                self.building_x = 0
            else:
                self.building_x += 2
        
        if t % 1 == 0:
            if self.mosque_y <= self.movie_layer.get_height() - self.mosque.get_height() - 200:
                self.mosque_y = self.movie_layer.get_height() - self.mosque.get_height() - 200
            else:
                self.mosque_y -= 3
            
            if self.building_y <= self.movie_layer.get_height() - self.building.get_height() - 200:
                self.building_y = self.movie_layer.get_height() - self.building.get_height() - 200
            else:
                self.building_y -= 3
            
        if self.timer > 40:
            self.airplane1_y -= 6
            self.airplane2_y -= 6
            self.airplane3_y -= 6
            
            self.airplane2_x -= 1
            self.airplane3_x += 1

class scene5:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.line1 = pygame.image.load('img/anim/line 1.png')
        self.line1_x = 0
        
        self.line2 = pygame.image.load('img/anim/line 2.png')
        self.line2_x = 168
        
        self.background = pygame.image.load('img/anim/store.png')
        self.background_x = 0

        self.car1 = pygame.image.load('img/anim/car 0.png')
        self.car2 = pygame.image.load('img/anim/car 1.png')
        self.cars = [self.car1,self.car2]
        self.car_x = 724
        
    def draw(self,screen):
        self.movie_layer.blit(self.background,(self.background_x,102))
        self.movie_layer.blit(self.line2,(self.line2_x,170))
        self.movie_layer.blit(self.line1,(self.line1_x,122))
        self.car = self.cars[0]
        self.movie_layer.blit(self.car,(self.car_x,162))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        if self.background_x >= self.movie_layer.get_width() - self.background.get_width():
            if t % 3 == 0:
                self.background_x -= 3
                self.car_x -= 3
            if t % 4 == 0:
                self.line2_x -= 3
            if t % 5 == 0:
                self.line1_x -= 3
        if t % 8 == 0:
            self.cars = self.cars[-1:] + self.cars[:-1]

class scene6:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.political_map = pygame.image.load('img/anim/political map.png')
        
        self.stars = pygame.image.load('img/anim/stars.png')
        self.circle = pygame.image.load('img/anim/circle.png')
        self.stars_xy = (312,150)
        self.circle_xy = (390,234)

        self.marking = self.stars
        self.marking_xy = self.stars_xy
        self.timing = 0

    def draw(self,screen):
        self.movie_layer.blit(self.political_map,(0,102))
        self.movie_layer.blit(self.marking,self.marking_xy)
        
        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        self.timing += 1
        if self.timing >= 60:
            self.marking = self.circle
            self.marking_xy = self.circle_xy

class scene7:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.political_map = pygame.image.load('img/anim/political map.png')
        self.eutopia_small = pygame.image.load('img/anim/eutopia small.png')
        
        self.circle = pygame.image.load('img/anim/circle.png')
        self.circle_xy = (390,234)

        self.marking = self.circle
        self.marking_xy = self.circle_xy
        self.timing = 0
        self.opacity = 1

    def draw(self,screen):
        self.movie_layer.blit(self.political_map,(0,102))
        self.movie_layer.blit(self.marking,self.marking_xy)
        
        for i in range(self.opacity):
            self.movie_layer.blit(self.eutopia_small,(274,102))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        self.timing += 1
        if self.timing >= 20:
            if t % 3 == 0:
                self.opacity += 1

class scene8:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.political_map = pygame.image.load('img/anim/political map.png')
        self.eutopia_small = pygame.image.load('img/anim/eutopia small solid.png')
        
        self.timing = 0
        self.opacity = 1

        self.transparent_surface = pygame.Surface((800,600))
        self.transparent_surface.set_alpha(5)
        self.transparent_surface.fill((0,0,0))

        self.stars = [[68,316,2],[112,128,2],[140,248,2],[216,200,2],[266,248,2],[666,122,2],[698,338,2],[752,192,2]]
    
    def draw(self,screen):
        self.movie_layer.fill((0,0,0))
        
        self.movie_layer.blit(self.political_map,(0,102))
       
        for s in self.stars:
            self.transparent_surface.fill((255,255,255),(s[0],s[1],s[2],s[2]))
        self.movie_layer.blit(self.transparent_surface,(0,0))
        
        self.movie_layer.blit(self.eutopia_small,(274,102))
        
        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        self.timing += 1
        if self.timing >= 20:
            if t % 3 == 0:
                self.opacity += 1
                self.transparent_surface.set_alpha(self.opacity*10)
                self.transparent_surface.fill((0,0,0))

class scene9:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.eutopia_small = pygame.image.load('img/anim/eutopia small solid.png')
        self.mars = pygame.image.load('img/anim/mars.png')
        self.mars_xy = (612,172)
        
        self.stars = [[68,316,2],[112,128,2],[140,248,2],[216,200,2],[266,248,2],[666,122,2],[698,338,2],[752,192,2]]
    
    def draw(self,screen):
        self.movie_layer.fill((0,0,0))
        
        for s in self.stars:
            self.movie_layer.fill((255,255,255),(s[0],s[1],s[2],s[2]))
        
        self.movie_layer.blit(self.eutopia_small,(274,102))
        self.movie_layer.blit(self.mars,(self.mars_xy))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        pass

class scene10:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.rs = pygame.image.load('img/flags/rs.png')
        self.ch = pygame.image.load('img/flags/ch.png')
        self.ru = pygame.image.load('img/flags/ru.png')
        self.us = pygame.image.load('img/flags/us.png')
        self.tk = pygame.image.load('img/flags/tk.png')

        self.flags = [self.rs,self.ch,self.ru,self.us,self.tk]
        self.timer = 0

    def draw(self,screen):
        self.flag = self.flags[0]
        self.movie_layer.blit(self.flag,(0,102))

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        self.timer += 1
        if self.timer <= 100:
            if t % 20 == 0:
                self.flags = self.flags[-1:] + self.flags[:-1]
        elif self.timer > 100 and self.timer <= 160:
            if t % 10 == 0:
                self.flags = self.flags[-1:] + self.flags[:-1]
        elif self.timer > 160 and self.timer <= 285:
            if t % 5 == 0:
                self.flags = self.flags[-1:] + self.flags[:-1]
        else:
            if t % 2 == 0:
                self.flags = self.flags[-1:] + self.flags[:-1]

class scene11:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer

        self.hand_l = pygame.image.load('img/anim/hand l.png')
        self.hand_r = pygame.image.load('img/anim/hand r.png')
        self.handshake = pygame.image.load('img/anim/handshake.png')
        self.flag = pygame.image.load('img/flags/eu.png')

        self.hand_l_x = -300
        self.hand_r_x = 492

        self.handshake_xy = (-176,136)
        
        self.timer = 0
        self.hands_shaking = False

    def draw(self,screen):
        self.movie_layer.blit(self.flag,(0,102))

        if not self.hands_shaking:
            self.movie_layer.blit(self.hand_l,(self.hand_l_x,148))
            self.movie_layer.blit(self.hand_r,(self.hand_r_x,198))
        else:
            self.movie_layer.blit(self.handshake,self.handshake_xy)

        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t):
        self.timer += 1
        if self.timer <= 70:
            if t % 3:
                self.hand_l_x += 2
                self.hand_r_x -= 2
        elif self.timer > 70 and self.timer <= 120:
            if t % 3:
                self.hand_l_x -= 3
                self.hand_r_x -= 1
        elif self.timer > 120 and self.timer <= 150:
            if t % 3:
                self.hand_l_x += 2
                self.hand_r_x -= 2
        
        else:
            self.hands_shaking = True

class scene12:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer
        self.seconds = 180
        self.font = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',50)

    def draw(self,screen):
        self.movie_layer.fill((0,0,0))
        
        timestr = str(datetime.timedelta(seconds=self.seconds))
        self.time = self.font.render(timestr,1,(120,20,20))
        self.time_rect = self.time.get_rect()
        self.time_rect.centerx = screen.get_rect().centerx
        self.time_rect.y = 230
        
        self.movie_layer.blit(self.time,self.time_rect)
        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t,TICK):
        if t % TICK == 0:
            self.seconds -= 1

class scene13:
    def __init__(self,screen,previous):
        self.movie_layer = previous.movie_layer
        self.seconds = previous.seconds
        self.font = previous.font
    
    def draw(self,screen):
        self.movie_layer.fill((0,0,0))
        
        timestr = str(datetime.timedelta(seconds=self.seconds))
        self.time = self.font.render(timestr,1,(120,20,20))
        self.time_rect = self.time.get_rect()
        self.time_rect.centerx = screen.get_rect().centerx
        self.time_rect.y = 230
        
        self.movie_layer.blit(self.time,self.time_rect)
        screen.blit(self.movie_layer,(0,0))
    
    def change(self,t,TICK):
        if t % TICK == 0:
            self.seconds -= 1
