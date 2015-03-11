import pygame

class Minister:
    def __init__(self,ministry,x,y):
        self.ministry = ministry
        self.x = x
        self.y = y
        self.cost = 100
        self.bribe_rate = 50
        self.bribe_time = 0
        self.restriction = 0
        self.bribe_times = [0,10,20,30]

        self.img = pygame.image.load('img/minister/minister%s.png' % ministry)
        self.scroll_bgs = [(78,144,94),(196,202,131),(174,138,99),(104,49,49)]
        self.scroll_img = pygame.image.load('img/scroll.png')
        self.scroll_button = pygame.Surface((self.scroll_img.get_width(),self.scroll_img.get_height()))
        self.animate_scroll = 0
        self.bill_pos = 0
        self.bill_img = pygame.image.load('img/bill.png')
        self.bill = pygame.Surface((self.bill_img.get_width(),self.bill_img.get_height()))
        self.bribe_img = pygame.image.load('img/bribe.png')

        pygame.font.init()
        self.font = pygame.font.Font('font/minecrafter/Minecrafter_3.ttf',15)

    def bribe(self,progress):
        progress.money -= self.cost
        self.cost = self.cost/2
        
        if self.restriction > 0:
            self.restriction -= 1
        else:
            self.restriction = 0

        self.bribe_time = self.bribe_times[self.restriction]

    def checkCost(self):
        self.bribe_time += 1
        self.cost += self.bribe_rate
        
        if self.bribe_time > self.bribe_times[1] and self.bribe_time <= self.bribe_times[2]:
            self.restriction = 1
        elif self.bribe_time > self.bribe_times[2] and self.bribe_time <= self.bribe_times[3]:
            self.restriction = 2
        elif self.bribe_time > self.bribe_times[3]:
            self.restriction = 3
        else:
            self.restriction = 0

    def scroll(self):
        #restriction color
        self.scroll_button.fill(self.scroll_bgs[self.restriction])
        
        #flip ako treba
        self.scroll_button.blit(self.scroll_img,(0,0))
        self.draw_text()
        return self.scroll_button

    def animateScroll(self):
        self.bill_pos += self.animate_scroll * 10

        if self.bill_pos < 0:
            self.bill_pos = 0
            self.animate_scroll = 0
            return False
        
        elif self.bill_pos >= self.img.get_width() + self.scroll_img.get_width():
            self.bill_pos = self.img.get_width() + self.scroll_img.get_width()
            self.bill.blit(self.bill_img,(0,0))
            self.draw_text()
            return True

        else:
            self.bill.blit(self.bill_img,(0,0))
            self.draw_text()
            return True

    def draw_text(self):
        cost_text = self.font.render('cost: %s' % self.cost,1,(0,0,0))
        self.bill.blit(cost_text,(10,10))
