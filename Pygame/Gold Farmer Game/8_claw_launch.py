import pygame
import os

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center = position) # center를 통해 해당 좌표를 rect의 중간값으로 정의할 수 있다.
        
        self.offset = pygame.math.Vector2(default_offset_x_claw, 0) # x위치를 100만큼 오른쪽으로 이동
        self.position = position
        
        # 집게의 회전구현 (10도에서 170도까지만 게임상에서 움직이도록 할 예정)
        self.direction = LEFT # 집게의 이동방향
        self.angle_speed = 2.5 # 집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10 # 최초 각도는 10도 (오른쪽 끝)
        
    def update(self, to_x): # sprite class가 제공하는 method로 sprite의 움직임을 도와주는 함수이다.(캐릭터가 숨쉬는 듯한 모션 구현에 사용)
        if self.direction == LEFT: # 왼쪽 방향으로 이동하고 있다면
            self.angle += self.angle_speed # 이동 속도만큼 각도 증가
        elif self.direction == RIGHT: # 오른쪽 방향으로 이동하고 있다면
            self.angle -= self.angle_speed
            
        # 만약에 허용 각도 범위를 벗어나면
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)
            
        # offset에서 x만 넣었음에도 각도에 따른 x, y좌표를 rotate method에서 처리해주기 때문에 발사해서 좌표가 변할때도 x만 변화를 주어도 된다.
        self.offset.x += to_x
        self.rotate() # 회전 처리
            
        # print(self.angle, self.direction) 잘 작동하는지 테스트
        
        # rect_center = self.position + self.offset # 원래의 position에 offset만큼 더해져서 center값이 정해진다.
        # self.rect = self.image.get_rect(center = rect_center)
        
    def rotate(self):
        # pygame.transform.rotate() 회전처리 함수는 두개지만 아래의 함수가 더 매끄럽다. 
        # rotozoom method는 원래의 이미지를 가지고 새로운 이미지를 생성해내는 방식으로 이미지의 회전을 구현한다. 따라서 원본이미지의 변수를 위에서 만들어준다.
        # 실제 각도는 반시계방향으로 커지기 때문에, 게임상에서 시계방향 각도 증가를 만들기 위해서는 각도에 -를 붙혀주어야 한다.
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1) # (원본이미지, 각도, 이미지 크기(변경x = 1))
        
        # 각도의 회전만큼 띄어주는 중심점으로부터 띄워주는 거리(offset)도 계속 변화해야함
        # Vector2 class에는 rotate라는 각에 따른 좌표변화를 자동으로 계산해주는 method가 다.
        offset_rotated = self.offset.rotate(self.angle)
        
        # 회전된 이미지가 새로 만들어질때마다 rect의 center값도 계속해서 달라지므로 rect도 새롭게 초기화를 계속 해주어야한다.
        # 이 과정을 진행하지 않으면 rect정보는 최초의 것을 계속 사용하기 때문에 이미지의 회전이 올바르지 않게 된다.
        # 중심점은 최초의 position을 계속 사용하되 이미지의 크기에 맞게 rect사이즈만 바꿔줌        
        self.rect = self.image.get_rect(center = self.position + offset_rotated)
        
        # print(self.rect)
        pygame.draw.rect(screen, RED, self.rect, 1)
        
    def set_direction(self, direction):
        self.direction = direction
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시
        # 중심점으로부터 집게까지의 직선을 그려줌
        pygame.draw.line(screen, BLACK, self.position, self.rect.center,  5) # line 함수를 통해 직선그리기, (어디에 그릴건지, 무슨색인지, 어디서부터, 어디까지, 두께)
        
    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite): # pygame의 sprite class를 상속받음
    def __init__(self, image, position):
        super().__init__() # sprite class의 초기화
        # sprite class를 상속받아서 사용하기 위해서는 반드시 2개의 member variable이 필요하다.
        self.image = image
        # 초기 위치가 보석마다 다 다르기 때문에 instance 생성 시 position을 받아오고, 그 값을 rect값의 center에 넣어준다.
        self.rect = image.get_rect(center = position)

def setup_gemstone(): # 게임에 원하는 만큼의 보석을 정의
    # 작은 금
    small_gold = Gemstone(gemstone_images[0], (200, 380))
    gemstone_group.add(small_gold) # 그룹에 추가
    # 큰 금 (여기서부턴 보석정의와 그룹추가를 한줄에 진행)
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

# 게임 관련 변수
default_offset_x_claw = 40 # 중심점으로부터 집게까지의 기본 x 간격
to_x = 0 # x 좌표 기준으로 집게 이미지를 이동시킬 값 저장 변수

# 속도 변수
move_speed = 12 # 발사할 때 이동 스피드 (x 좌표 기준 증가되는 값)
return_speed = 20 

# 방향 변수
LEFT = -1 # 왼쪽 방향
STOP = 0 # 방향이 멈출때, 방향이 없으니 0으로 정의
RIGHT = 1 # 오른쪽 방향

# 색깔 변수
RED = (255, 0, 0)
BLACK = (0, 0, 0)

current_path = os.path.dirname(__file__)
image_path  = os.path.join(current_path, "game_image")
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(image_path, "small_gold.png")),
    pygame.image.load(os.path.join(image_path, "big_gold.png")),
    pygame.image.load(os.path.join(image_path, "stone.png")),
    pygame.image.load(os.path.join(image_path, "diamond.png"))]

# 보석 그룹 (보석은 여러개니까 여러 개를 만들고 그리는 것도 여러개를 한번에)
gemstone_group = pygame.sprite.Group()
setup_gemstone()

# 집게
claw_image = pygame.image.load(os.path.join(image_path, "claw.png"))
claw = Claw(claw_image, (screen_width // 2, 110)) # 가로위치는 화면 기준 절반, 세로위치는 위에서 110px (//연산자는 나눗셈 후 소숫점 부분을 버려줌)

running = True
while(running):
    clock.tick(30) # FPS 값이 30으로 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            claw.set_direction(STOP) # 좌우 멈춤
            to_x = move_speed # move_speed만큼 빠르게 쭉 뻗음
            
    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed
        
    if claw.offset.x < default_offset_x_claw : # 원위치에 오면
        to_x = 0
        claw.set_init_state() # 처음 상태로 되돌림
    
    screen.blit(background, (0, 0))
    
    gemstone_group.draw(screen) # 그룹에 있는 모든 sprite들을 screen에 그려줌 (draw함수는 group class에서만 사용가능)
    claw.update(to_x)
    claw.draw(screen) # claw는 group이 아니기 때문에 draw method가 없다. 따라서 Claw class에서 draw method를 정의해줬다.
    
    pygame.display.update()
                
pygame.quit()