import pygame,datetime
from random import randint

class Progress:
    def __init__(self,money,goal,time):
        self.money = money
        self.goal = goal
        self.time = time
        self.payup = 0
        self.last_payment = 0

    def get_progress(self):
        #returns progress in percents
        return self.payup * 100 / self.goal

class Score:
    def __init__(self):
        self.objects = {0:[0,0,0],1:[0,0,0],2:[0,0,0],3:[0,0,0],4:[0,0,0],5:[0,0,0]}
        
    def sold(self,obj,lvl):
        self.objects[obj][lvl] += 1

class Bar:
    def __init__(self,screen):
        self.img = pygame.image.load('img/eumeter/bar.png')
        self.x = screen.get_width() - self.img.get_width()
        self.y = 20
        self.bar = pygame.Surface((self.img.get_width(),self.img.get_height()))
    
    def draw(self,progress):
        progress_h = progress * 546 / 100

        #shade
        self.bar.fill((108,46,34),(16,562-progress_h,2,progress_h))
        #main
        self.bar.fill((138,49,31),(18,562-progress_h,6,progress_h))
        self.bar.blit(self.img,(0,0))
        return self.bar

class Displays:
    def __init__(self,screen):
        self.img = pygame.image.load('img/eumeter/displays.png')
        self.x = screen.get_width() - self.img.get_width()
        self.y = 0
        self.displays = pygame.Surface((self.img.get_width(),self.img.get_height()),pygame.SRCALPHA,32)
        self.displays = self.displays.convert_alpha()
        pygame.font.init()
        self.font1 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',23)
        self.font2 = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',11)
        
        self.old_t = 6
    
    def draw(self,cash,time,t):
        money = self.font2.render('%sk eur' % cash,1,(255,255,102))
        money_x = 173 - money.get_width()
        money_y = 91

        if time <= 10:
            timecolor = (138,49,31)
        else:
            timecolor = (145,155,148)

        timestr = str(datetime.timedelta(seconds=time)).split(':')

        time_m = self.font1.render(timestr[1],1,timecolor)
        time_m_x = 26
        time_m_y = 25

        time_s = self.font1.render(timestr[2],1,timecolor)
        time_s_x = 87
        time_s_y = 25
        
        new_t = randint(0,5)
        while new_t == self.old_t:
            new_t = randint(0,5)
        
        time_f = self.font1.render('%s%s' % (new_t,(9-t%10)),1,timecolor)
        time_f_x = 146
        time_f_y = 25

        self.displays.blit(self.img,(0,0))
        self.displays.blit(money,(money_x,money_y))
        self.displays.blit(time_m,(time_m_x,time_m_y))
        self.displays.blit(time_s,(time_s_x,time_s_y))
        self.displays.blit(time_f,(time_f_x,time_f_y))
        
        self.old_t = new_t
        
        return self.displays

class Kosovo_display:
    def __init__(self,x):
        self.img = pygame.image.load('img/eumeter/k-display.png')
        self.x = x - self.img.get_width() + 26
        self.y = 6

    def draw(self):
        #pozicija zavisi od animacije
        return self.img

class Paybutton:
    def __init__(self,screen):
        self.img = pygame.image.load('img/eumeter/pay-off.png')
        self.img_pressed = pygame.image.load('img/eumeter/pay-on.png')
        self.pressed = False
        self.x = screen.get_width() - self.img.get_width() - 40
        self.y = 114

    def draw(self):
        #animacija
        if self.pressed == True:
            return self.img_pressed
        else:
            return self.img
