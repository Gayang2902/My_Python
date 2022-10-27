import pygame
import os

# 보석 클래스
class Gemstone(pygame.sprite.Sprite): # pygame의 sprite class를 상속받음
    def __init__(self, image, position):
        super().__init__() # sprite class의 초기화
        # sprite class를 상속받아서 사용하기 위해서는 반드시 2개의 member variable이 필요하다.
        self.image = image
        # 초기 위치가 보석마다 다 다르기 때문에 instance 생성 시 position을 받아오고, 그 값을 rect값의 center넣어준다.
        self.rect = image.get_rect(center = position)

def setup_gemstone(): # 게임에 원하는 만큼의 보석을 정의
    # 작은 금
    small_gold = Gemstone(gemstone_images[0], (200, 380))
    gemstone_group.add(small_gold) # 그룹에 추가
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 380)))

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path  = os.path.join(current_path, "game_image")
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(image_path, "small_gold.png")),
    pygame.image.load(os.path.join(image_path, "big_gold.png")),
    pygame.image.load(os.path.join(image_path, "stone.png")),
    pygame.image.load(os.path.join(image_path, "diamond.png"))]

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone()

running = True
while(running):
    clock.tick(30) # FPS 값이 30으로 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    
    gemstone_group.draw(screen) # 그룹에 있는 모든 sprite들을 screen에 그려줌
    
    pygame.display.update()
                
pygame.quit()