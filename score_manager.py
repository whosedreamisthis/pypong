import pygame
from consts import *
pygame.font.init() 

font = pygame.font.Font(None, 80)

class ScoreManager:
    def __init__(self):
        self.player_score = 0
        self.enemy_score = 0
        self.player_score_pos = (SCREEN_WIDTH//2 + 50,50)
        self.enemy_score_pos = (SCREEN_WIDTH//2 - 50 + 20,50)
    
    def increase_player_score(self):
        self.player_score += 1
        
    def increase_enemy_score(self):
        self.enemy_score += 1
        
    def draw(self, screen):
        player_text_surface = font.render(f"{self.player_score}", True,OFFWHITE ) # Text, Antialias, Color
        player_text_rect = player_text_surface.get_rect(midleft=self.player_score_pos)
        screen.blit(player_text_surface, player_text_rect)
        
        enemy_text_surface = font.render(f"{self.enemy_score}", True,OFFWHITE ) # Text, Antialias, Color
        enemy_text_rect = enemy_text_surface.get_rect(midright=self.enemy_score_pos)
        screen.blit(enemy_text_surface, enemy_text_rect)
        
    def update(self):
        pass
        