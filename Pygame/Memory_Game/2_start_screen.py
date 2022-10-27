import pygame

# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) # draw 함수를 이용해 원 그리기 (어디에 그릴건지, 색, , 중심좌표, 반지름, 두께 )

pygame.init()

# 가로 격자 9, 세로 격자 5 // 격자 하나당 120*120px 사용
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120) # 이미지 없이 Rect class를 이용해서 rectangle을 만들 수 있다.(top, left, width, height)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)
    
    # 시작 화면 표시
    display_start_screen()
    
    pygame.display.update()
    
pygame.quit()