import pygame
from consts import *

class Paddle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.speed = 4
        
    def move_up(self):
        self.y -= self.speed
        if self.y < self.height/2:
            self.y = self.height/2

    
    def move_down(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT - self.height/2:
            self.y = SCREEN_HEIGHT - self.height/2        
    def draw(self,screen):
        pygame.draw.rect(screen,OFFWHITE, (self.x,self.y - self.height//2,self.width,self.height))
        
        
        