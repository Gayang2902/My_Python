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

background = pygame.image.load(os.path.join(image_path, "background.png"))
#background = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Pygame/game image/background.png")

# stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Pygame/game image/stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1] # stage 위에 character를 세워놓기 위해 계산을 통한 변수생성

# character = pygame.image.load(os.path.join(image_path), "character.png")
character = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Pygame/game image/character.png")
character_size = character.get_rect().size  
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height

character_to_x = 0

character_speed = 5

weapon = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Pygame/game image/weapon.png")
weapon_size = weapon.get_rect().size    
weapon_width = weapon_size[0]   

weapons = []

weapon_speed = 10

ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

balls = []

# 공은 여러개가 존재하고 각각 좌우상하 움직임이 다르기 때문에 dictionary를 이용해 세분화 시켜준다. 아래는 최초 발생하는 큰 공
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "image_index" : 0,
    "to_x" : 3, 
    "to_y" : -6,
    "init_speed_y" : ball_speed_y[0]})

# 사라질 무기와 공이 가지게 될 index(무기와 공이 닿으면 무기는 사라지고, 공은 사라진뒤 해당 자리에 작은 공이 생김)
ball_to_remove = -1
weapon_to_remove = -1

running = True
while running:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                #weapon_y_pos = screen_height - stage_height - character_height
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
    character_x_pos += character_to_x
        
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    # weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # 한 줄 for문은 이런식으로
    for w in weapons: # 정석 for문은 이런식으로
        w[1] = w[1] - weapon_speed
        
    # 천장에 닿지 않은 weapon들만 리스트에 재저장핢으로써 천장에 닿은 weapon은 리스트에 들어가지 않기에 더는 그려지지 않는다.
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    
    # 공 위치 정의
    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_image_index = ball_value["image_index"]
        
        ball_size = ball_images[ball_image_index].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        if ball_pos_x <= 0 or ball_pos_x >= screen_width - ball_width:
            ball_value["to_x"] *= -1
            
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_value["to_y"] = ball_value["init_speed_y"]
        else:
            ball_value["to_y"] += 0.5
            
        ball_value["pos_x"] += ball_value["to_x"]
        ball_value["pos_y"] += ball_value["to_y"]

    # 각 개체들의 rect 정보 업데이트(위치가 먼저 정의되어야 하기 때문에 위치 정의 파트 아래에 작성)
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_image_index = ball_value["image_index"]
        
        ball_rect = ball_images[ball_image_index].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        
        if character_rect.colliderect(ball_rect):
            running = False
            break
        
        for weapon_index, weapon_value in enumerate(weapons):
            weapon_pos_x = weapon_value[0]
            weapon_pos_y = weapon_value[1]
            
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_index
                ball_to_remove = ball_index
                
                # 가장 작은 공이 아닐 경우, 다음 단계의 공으로 나눠지는 처라
                if ball_index < 3:
                    # 현재 공의 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1
                                                 
                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_image_index + 1].get_rect
                    
                    # 왼쪽으로 나눠지는 공 // 2:23:53
                    balls.append({
                        "pos_x" : 50,
                        "pos_y" : 50,
                        "image_index" : ball_value["image_index"] + 1,
                        "to_x" : -3,
                        "to_y" : -6,
                        "inint_speed_y" : ball_speed_y[0]})
                    
                break
            
    # 충돌된 공 or 무기 없애기 
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
        
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
            
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    for index, value in enumerate(balls):
        ball_pos_x = value["pos_x"]
        ball_pos_y = value["pos_y"]
        ball_image_index = value["image_index"]
        screen.blit(ball_images[ball_image_index], (ball_pos_x, ball_pos_y))
    
    screen.blit(character, (character_x_pos, character_y_pos))        
    screen.blit(stage, (0, screen_height - stage_height))
    
    pygame.display.update()
    
pygame.quit()