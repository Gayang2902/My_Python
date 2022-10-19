import pygame
from random import *

################################################################
## 기본 초기화 (반드시 해야 하는 것들)

pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

# FPS
clock = pygame.time.Clock(30)
################################################################

################################################################

## 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("/Users/kduk/Desktop/Python/활용/Game/background.png")

character = pygame.image.load("/Users/kduk/Desktop/Python/활용/Game/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]    
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 0.5
enemy_speed = 0.3

enemy = pygame.image.load("/Users/kduk/Desktop/Python/활용/Game/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, (480 - enemy_width))
enemy_y_pos = 0

game_font = pygame.font.Font(None, 40)

running = True 
while running:
    dt = clock.tick(30) 

    ## 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos = to_x * dt

    for enemy_drop in range(0, (640 - enemy_width)):
        enemy_y_pos += enemy_drop
        if enemy_y_pos == (screen_height - enemy_height):
            enemy_y_pos == 0
            enemy_x_pos == randint(0, (480 - enemy_width))
            
    ## 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt 
    character_y_pos += to_y * dt

    ## 4. 충돌 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    ## 5. 화면에 그리기

    pygame.display.update() 

# 게임종료 => pygame 종료 
pygame.quit()  

