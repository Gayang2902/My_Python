import pygame

pygame.init()   

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game")

# FPS 설정
clock = pygame.time.Clock()

background = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/background.png")

character = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/character.png")
character_size = character.get_rect().size # 이미지의 크기 구하기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

enemy = pygame.image.load("/Users/kd_mb/Desktop/code/Python/Game/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트정의먼저
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시각 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

running = True
while running:
    fps = clock.tick(60) # 게임 프레임 설정

    # 캐릭터가 1초 동안에 100만큼 이동해야한다고 가정하면(프레임에 따른 게임의 움직임 비교)
    # 10 fps 에서는 1초 동안에 10번 동작 -> 1번에 10만큼 이동해야함 => 10 * 10 = 100
    # 20 fps 에서는 1초 동안에 5번 동작 -> 1번에 5만큼 이동해야함 => 20 * 5 = 100

    print("fps : " + str(clock.get_fps()))

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
 
    character_x_pos += to_x * fps # 위에 주석내용을 참고로 이동속도 * 프레임을 해줘야지  
    character_y_pos += to_y * fps # 서로다른 프레임에서도 같은 게임속도를 유지할 수 있다.

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("CRUSH")
        running = False

    # screen.fill((0, 0, 255)) # 단순하게 색을 튜플형태의 rgb로 채워넣을수 있다.
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타미어 집어넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # time.get_ticks 함수의 반환값은 ms이다.
    # tick은 시간이 지날수록 계속 카운팅되는데 게임을 진행하면서 계속 올라간 시간 - 처음 시작 시각을 해주면 경과시간이 된다.

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 초 단위표시를 위해 int를 사용
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time < 0:
        print("TIME OUT")
        running = False

    pygame.display.update() # 화면을 계속 그려줘야함

pygame.time.delay(2000) # 2초 정도 종료대기

pygame.quit()