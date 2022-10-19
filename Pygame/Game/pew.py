# quiz : 똥피하기 게임

import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("PEW GAME")

clock = pygame.time.Clock()

background = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/background.png")

character = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 0.3
to_x = 0
to_y = 0

pew = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/enemy.png")
pew_size = pew.get_rect().size
pew_width = pew_size[0]
pew_height = pew_size[1]
pew_x_pos = random.randint(0, screen_width - pew_width)
pew_y_pos = 0

running = True

while running:
    fps = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * fps
    character_y_pos += to_y * fps

    pew_y_pos += character_speed * fps
    if pew_y_pos > screen_height - pew_height:
        pew_x_pos = random.randint(0, screen_width - pew_width)
        pew_y_pos = pew_height

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_xpos = screen_width - character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    pew_rect = pew.get_rect()
    pew_rect.left = pew_x_pos
    pew_rect.top = pew_y_pos

    if character_rect.colliderect(pew_rect):
        running = False
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(pew, (pew_x_pos, pew_y_pos))

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()

# # https://www.youtube.com/watch?v=QU1pPzEGrqw