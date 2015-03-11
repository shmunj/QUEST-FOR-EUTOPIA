import pygame
from random import randint

class Node:
    def __init__(self,position):
        self.position = position
        self.building = None
        self.wait = 0

    def drawOnMap(self,map):
        (self.position[0] + map.x,self.position[1] + map.y)

class Building:
    def __init__(self,object_type,node,key):
        self.node = node
        self.object_type = object_type
        self.key = key #key in the buildings dictionary
        node.building = self

        if self.object_type == 6:
            self.special_types = ['orthodox temple','war criminal','scientist','santa','soccer player','mobster','treasure','mystery briefcase']
            self.special_values = [1000,1000,1000,1000,1000,1000,1000,1000]
            self.special_backfire_chances = [20,20,20,20,20,20,20,20] #chance for bad outcome after the sale
            
            self.level = randint(0,7) #broj specijalnih objekata
            self.special_type = self.special_types[self.level]
            self.value = self.special_values[self.level]
            self.special_backfire_chance = self.special_backfire_chances[self.level]
            self.growth = 50
            self.img = pygame.image.load('img/objects/%s/%s.png' % (self.object_type,self.level))
        
        else:
            self.value = 50
            self.level = 0
            self.growth = 0
            self.img = pygame.image.load('img/objects/%s/%s.png' % (self.object_type,self.level))
        
        #animacija

    def sell(self,can_sell,progress,score):
        if can_sell == True:
            progress.money += self.value
            #zvuk
            #animacija
                #(neklikljivo)
            if self.object_type != 6:
                score.sold(self.object_type,self.level)
        else:
            print 'can\'t sell this'

    def checkGrowth(self):
        if self.object_type <= 5:
            self.growth += 1
            
            if self.growth > 20 and self.growth <= 40:
                if self.level == 0:
                    self.grow()
                self.level = 1
                self.value = 500
            elif self.growth > 40:
                if self.level == 1:
                    self.grow()
                self.level = 2
                self.value = 1000
            else:
                self.level = 0
                self.value = 250

    def grow(self):
        self.level += 1 #ubij ovo posle
        self.img = pygame.image.load('img/objects/%s/%s.png' % (self.object_type,self.level))
        
        #animacija
        #(neklikljivo dok animira)

    def special(self):
        print 'SPECIAL:', self.special_type
        
        #backfire
        if randint(1,self.special_backfire_chance) == self.special_backfire_chance:
            print 'BACKFIRE!!!'
            #backfire function
        else:
            print 'OK'
