import pygame, random
from consts import *

class Ball:
    def __init__(self):
        self.speed = 2
        self.dx = random.choice([-1, 1]) # Initial horizontal direction (-1 for left, 1 for right)
        self.dy = random.choice([-1, 1])
        self.radius = 10
        self.x = SCREEN_WIDTH // 2 + self.radius
        self.y = SCREEN_HEIGHT // 2 + self.radius

    def reset(self):
        self.x = SCREEN_WIDTH // 2 + self.radius
        self.y = SCREEN_HEIGHT // 2 + self.radius
        self.dx = random.choice([-1, 1]) # Initial horizontal direction (-1 for left, 1 for right)
        self.dy = random.choice([-1, 1])
                
    def draw(self,screen):
        pygame.draw.circle(screen, OFFWHITE,(self.x, self.y),self.radius)
        
    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        
        if self.y < self.radius:
            self.y = self.radius
            self.dy *= -1
        if self.y > SCREEN_HEIGHT - self.radius:
            self.y = SCREEN_HEIGHT - self.radius
            self.dy *= -1
        
        