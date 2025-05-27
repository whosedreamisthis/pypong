import pygame
from consts import *
from score_manager import ScoreManager
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 60
running = True
score_manager = ScoreManager()
def draw_line(screen):
    segment_length = 30
    gap_length = 20
    
    current_y = 0
    num_iterations = SCREEN_WIDTH // (segment_length + gap_length)
    x = SCREEN_WIDTH//2
    for n in range(num_iterations):
        pygame.draw.rect(screen,OFFWHITE, (x, current_y,20,segment_length))
        
        current_y += segment_length + gap_length
    # pygame.draw.rect(screen,BLACK, (SCREEN_WIDTH//2,0,32,SCREEN_HEIGHT))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    draw_line(screen)
    score_manager.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    
            
pygame.quit()