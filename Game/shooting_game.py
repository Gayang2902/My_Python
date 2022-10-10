# 오락실 pang 게임

# [게임 조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 2. 스페이스를 누르면 무기를 쏘아 올림
# 3. 큰 공 1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공을 없애면 게임 종료 (성공)
# 6. 캐릭터는 공에 닿으면 게임 종료 (실패)
# 7. 시간 제한 99초 초과 시 게임 종료 (실패)
# 8. FPS는 30으로 고정 (필요 시 speed 값을 조정)

# [게임 이미지]
# 1. 배경 : 640 * 480
# 2. 무대 : 640 * 50
# 3. 캐릭터 : 33 * 60
# 4. 무기 : 20 * 430
# 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20

import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pang")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path, "game image")

# background = pygame.image.load(os.path.join(image_path, "background.png"))
background = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/game image/background.png")

# stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/game image/stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1] # stage 위에 character를 세워놓기 위해 계산을 통한 변수생성

# character = pygame.image.load(os.path.join(image_path), "character.png")
character = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/game image/character.png")
character_size = character.get_rect().size  
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) + (character_width / 2)
character_y_pos = screen_height - stage_height - character_height

running = True
while running:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()
    
pygame.quit()