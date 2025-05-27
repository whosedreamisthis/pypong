import pygame,random
from consts import *
from score_manager import ScoreManager
from paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 60
running = True
score_manager = ScoreManager()
player = Paddle (SCREEN_WIDTH - 30,SCREEN_HEIGHT//2)
enemy = Paddle (30,SCREEN_HEIGHT//2)
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

def move_enemy():
    pass
    # do_it = random.choice([0,1,2])
    # if do_it == 0:
    #     enemy.move_down()
    # else:
    #     enemy.move_up()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move_up()
    elif keys[pygame.K_DOWN]:
        player.move_down()
    
    move_enemy()
    screen.fill(BLACK)
    draw_line(screen)
    score_manager.draw(screen)
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    
            
pygame.quit()