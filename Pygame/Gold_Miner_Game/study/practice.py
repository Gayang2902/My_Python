import math
import pygame

# 라디안 각을 사용하는 함수
rad_angle = round(math.radians(90), 3)
print(rad_angle)
rad_angle = round(math.radians(180), 3)
print(rad_angle)
rad_angle = round(math.radians(0), 3)
print(rad_angle)

# 시스템에서 pygame에 사용가능한 폰트들을 확인가능
print(pygame.font.get_fonts())