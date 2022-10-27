import pygame

pygame.init()

# 가로 격자 9, 세로 격자 5 / 격자 하나당 100*100px 사용
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(screen, (0, 0))
    
    pygame.display.update()
    
pygame.quit()