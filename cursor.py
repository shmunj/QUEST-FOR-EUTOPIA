import pygame

class Cursor:
    def __init_(self):
        self.img = pygame.image.load('img/cursor/default.png')
        pygame.mouse.set_visible(0)

    def normal(self):
        self.img = pygame.image.load('img/cursor/default.png')
        pygame.mouse.set_visible(0)

    def sell(self):
        self.img = pygame.image.load('img/cursor/sell.png')
        pygame.mouse.set_visible(0)
    
    def cant_sell(self):
        self.img = pygame.image.load('img/cursor/sell-r.png')
        pygame.mouse.set_visible(0)

    def bribe(self):
        #da nestane default cursor
        self.img = pygame.image.load('')
