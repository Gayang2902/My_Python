import enum
import pygame
import random

# 레벨에 맞게 설정
def setup(level):
    # 얼마동안 숫자를 보여줄지
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1) # 레벨이 아무리 높아져도 1초는 보여주어야 하니, max함수를 이용해 최소한 1초는 보여주도록 한다.
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) # 내장함수인 min함수는 parameter 중 더 작은 값을 반환해준다.

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)
    
# 숫자 섞기 (이 프로젝트에서 가장 중요)
def shuffle_grid(number_count):
    rows = 5
    columns = 9
    
    cell_size = 130 # 각 Grid cell 별 가로, 세로 크기
    button_size = 110 # Grid cell 내에 실제로 그려질 버튼의 크기
    screen_left_margin = 50 # 전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백
    
    grid = [[0 for col in range(columns)] for row in range(rows)] # 5 x 9 의 이차원 리스트를 만들고 0으로 채워넣는다
    
    number = 1 # 시작 숫자 1부터 number_count 까지, 만약 5라면 5까지 숫자를 랜덤으로 배치
    while number <= number_count:
        row_index = random.randrange(0, rows)
        column_index = random.randrange(0, columns)
        
        if grid[row_index][column_index] == 0:
            grid[row_index][column_index] = number # 숫자 지정
            number += 1
            
            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (column_index * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_index * cell_size) + (cell_size / 2)
            
            # 숫자 버튼 그리기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)
            
            number_buttons.append(button)
            
# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) # draw 함수를 이용해 원 그리기 (어디에 그릴건지, 색, , 중심좌표, 반지름, 두께 )

# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start, start_ticks
    if start: # 게임이 시작했다면
        check_number_buttons(pos)
    elif start_button.collidepoint(pos): # colliderect는 rectangle끼리의 접촉을 인식했다면 collidepoint는 rectangle과 좌표의 접촉을 인식해준다.
        start = True
        start_ticks = pygame.time.get_ticks() # 타이머 시작 (현재 시간을 저장)
        
def check_number_buttons(pos):
    global hidden
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]: # 올바른 숫자 클릭 (눌러야 하는 숫자는 항상 첫번째 인덱스에 존재하기 때문에(이전 숫자를 눌러서 리스트에서 제거되면 자동으로 인덱스 번호가 당겨진다.) pos와 접촉하는 button은 버튼리스트의 첫번째 값이다.)
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else: # 잘못된 숫자 클릭
                pass
            break

# 게임 화면 보여주기
def display_game_screen():
    global hidden
    
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
        if elapsed_time > display_time:
            hidden = True
    
    # hidden이 켜져있으면 눌러야하는 부분을 상자로만 표시해주고, hidden이 꺼져있으면 숫자를 표시해준다.
    for index, rect in enumerate(number_buttons, start = 1): # index와 실제 숫자를 맞춰주기 위해 start = 1로 index 보정을 해준다.
        if hidden: # 숨김 처리
            # 버튼 사각형 그리기
            pygame.draw.rect(screen, WHITE, rect) # 특정 rect를 그려주는 함수 (어디에 그릴지, 색, 어떤 rect인지)
        else:
            # 실제 숫자 텍스트
            cell_text = game_font.render(str(index), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            pygame.draw.rect(screen, (255, 0, 0), text_rect, 1)
            screen.blit(cell_text, text_rect)

pygame.init()

# 가로 격자 9, 세로 격자 5 // 격자 하나당 120*120px 사용
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) # 폰트 정의

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120) # 이미지 없이 Rect class를 이용해서 rectangle을 만들 수 있다.(top, left, width, height)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

number_buttons = [] # 플레이어가 눌러야 하는 버튼들
display_time = None # 숫자를 보여주는 시간
start_ticks = None # 시간 계산 (현재 시간 정보를 저장)

# 게임 시작 여부
start = False
# 숫자 숨김 여부 (사용자가 1을 클릭했거나, 보여주는 시간 초과했을 때)
hidden = False

# 게임 시작 전에 게임 설정 함수 수행
setup(1)

running = True

while running:
    click_pos = None
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos() # 마우스 커서의 좌표를 반환해주는 함수
            
    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)
    
    if start: 
        # 게임 화면 표시
        display_game_screen()
    else:
        # 시작 화면 표시
        display_start_screen()
    
    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)
    
    pygame.display.update()
    
pygame.quit()