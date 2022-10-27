from select import select
import pygame
import os
import random

class Player():
    number_bots = None

    def __init__(self):
        self.cards = []
    
    def get_card(self):
        self.cards.append(cards[random.randrange(DIAMOND_SHAPEM)][random.randrange(JACK_CARDM)])
        print(cards[0])
        
def make_text_blit(message, color, cent):
    text = game_font.render(message, True, color)
    text_rect = text.get_rect(center = cent)
    screen.blit(text, text_rect)        
        
def display_start_screen():
    
    make_text_blit("Choose numbers of bots", WHITE, (screen_width / 2, screen_height - 200))
    make_text_blit("1", WHITE, select_buttons[0].center)
    pygame.draw.circle(screen, WHITE, select_buttons[0].center, 70, 5)
    make_text_blit("2", WHITE, select_buttons[1].center)
    pygame.draw.circle(screen, WHITE, select_buttons[1].center, 70, 5)
    make_text_blit("3", WHITE, select_buttons[2].center)
    pygame.draw.circle(screen, WHITE, select_buttons[2].center, 70, 5)
    make_text_blit("4", WHITE, select_buttons[3].center)
    pygame.draw.circle(screen, WHITE, select_buttons[3].center, 70, 5)
    
def game_screen():
    pass
    
def check_button(pos):
    global start
    if start:
        print("START!")
    elif select_buttons[0].collidepoint(pos):
        Player.number_bots = 1
        start = True
    elif select_buttons[1].collidepoint(pos):
        Player.number_bots = 2
        start = True
    elif select_buttons[2].collidepoint(pos):
        Player.number_bots = 3
        start = True
    elif select_buttons[3].collidepoint(pos):
        Player.number_bots = 4
        start = True

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
screen_center_x = screen_width / 2
screen_center_y = screen_height / 2

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "game_image")

# 카드 관련 변수
ACE = 12
KING = 13
QUEEN = 14
JACK_CARDM = 15
SPADE = 1
HEART = 2
CLOVER = 3
DIAMOND_SHAPEM = 4

# 색 변수
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 게임 관련 변수
user_turn = True
start = False
click_pos = None

select_buttons = [pygame.Rect(0, 0, 120, 120) for i in range(4)]
select_buttons[0].center = (screen_center_x - 300, screen_center_y)
select_buttons[1].center = (screen_center_x - 100, screen_center_y)
select_buttons[2].center = (screen_center_x + 100, screen_center_y)
select_buttons[3].center = (screen_center_x + 300, screen_center_y)

cards = [[num for num in range(JACK_CARDM)] for shape in range(DIAMOND_SHAPEM)]
# print(cards)

# 폰트 정의
game_font = pygame.font.Font(None, 100)

running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
    
    screen.fill(BLACK)
    
    if start:
        pass
    else:
        display_start_screen()
        
    if click_pos:
        check_button(click_pos)          
    
    pygame.display.update()
    
# pygame.time.delay(2000)
pygame.quit()