import pygame
import os

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path  = os.path.join(current_path, "game_image")
background = pygame.image.load(os.path.join(image_path, "background.png"))


running = True
while(running):
    clock.tick(30) # FPS 값이 30으로 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    pygame.display.update()
                
pygame.quit()