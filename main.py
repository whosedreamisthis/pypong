import pygame,random
from consts import *
from score_manager import ScoreManager
from paddle import Paddle
from ball import Ball
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 60
running = True
paused = True
score_manager = ScoreManager()
player = Paddle (SCREEN_WIDTH - 30,SCREEN_HEIGHT//2)
enemy = Paddle (30,SCREEN_HEIGHT//2)
ball = Ball()

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

def check_out_of_bounds():
    global paused
    if ball.x < -ball.radius:
        score_manager.increase_player_score()
        ball.reset()
        paused = True
    elif ball.x > SCREEN_WIDTH:
        score_manager.increase_enemy_score()
        ball.reset()
        paused = True

def check_collision():
    if ball.x >= player.x - ball.radius\
        and player.y - player.height/2 <= ball.y <= player.y + player.height/2:
        ball.dx *= -1
        print(f"1 check collision: {ball.x} {ball.y} {ball.dx} {ball.dy}")
    elif ball.x < enemy.x + ball.radius + player.width /2\
        and enemy.y - enemy.height/2 <= ball.y <= enemy.y + enemy.height/2:
        ball.dx *= -1
        print(f"1 check collision: {ball.x} {ball.y} {ball.dx} {ball.dy}")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            
    if not paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move_up()
            enemy.move_up()
        elif keys[pygame.K_DOWN]:
            player.move_down()
            enemy.move_down()
        
        ball.update()
        check_out_of_bounds()
        check_collision()
        move_enemy()
    screen.fill(BLACK)
    draw_line(screen)
    score_manager.draw(screen)
    player.draw(screen)
    enemy.draw(screen)
    ball.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    
            
pygame.quit()