import pygame

pygame.init()   

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game")

background = pygame.image.load("/Users/kd_mb/Desktop/code/Python/활용/Game/background.png")

character = pygame.image.load("/Users/kd_mb/Desktop/code/Python/활용/Game/character.png")
character_size = character.get_rect().size # 이미지의 크기 구하기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.type == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # screen.fill((0, 0, 255)) # 단순하게 색을 튜플형태의 rgb로 채워넣을수 있다.
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 화면을 계속 그려줘야함

pygame.quit()