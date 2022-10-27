import pygame

pygame.init()

# 가로 격자 9, 세로 격자 5
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(screen, (0, 0))
    
    pygame.display.update()
    
pygame.quit()