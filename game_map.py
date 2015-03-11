import pygame,datetime
from random import randint

class Map:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img_with_kosovo = pygame.image.load('img/map/map.png')
        self.img_without_kosovo = pygame.image.load('img/map/map-k.png')
        
        self.img = self.img_with_kosovo
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        
        self.kosovo_sell_img = pygame.image.load('img/map/sell-k.png')
        self.kosovo_timer_img = pygame.image.load('img/map/k-timer.png')
        self.kosovo_sold = False
        self.kosovo_timeout = 30
        
        self.font = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',11)
        
        self.old_t = 6

    def get_kosovo_pos(self):
        return (self.x+290,self.y+760)

    def kosovo_counter(self,t):
        timestr = str(datetime.timedelta(seconds=self.kosovo_timeout)).split(':')

        time_m = self.font.render(timestr[1],1,(145,155,148))
        time_m_x = 44
        time_m_y = 30

        time_s = self.font.render(timestr[2],1,(145,155,148))
        time_s_x = 80
        time_s_y = 30

        new_t = randint(0,5)
        while new_t == self.old_t:
            new_t = randint(0,5)

        time_t = self.font.render('%s:%s' % (new_t,(9-t%10)),1,(145,155,148))
        time_t_x = 114
        time_t_y = 30

        timer = pygame.Surface((self.kosovo_timer_img.get_width(),self.kosovo_timer_img.get_height()),pygame.SRCALPHA,32)
        timer.convert_alpha()
        timer.blit(self.kosovo_timer_img,(0,0))
        timer.blit(time_m,(time_m_x,time_m_y))
        timer.blit(time_s,(time_s_x,time_s_y))
        timer.blit(time_t,(time_t_x,time_t_y))
        
        self.old_t = new_t

        return (timer,(self.x+240,self.y+770))
