import pygame
import sys
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
caption = pygame.display.set_caption('AERO MUSIC CENTER')
BG = (52,52,64)
time = pygame.time.Clock()
running = True
pygame.font.init()
font = pygame.font.SysFont('Arial', 45, bold = True)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BG)
    title = font.render('AERO MUSIC CENTRE',True , (255,255,255))
    screen.blit(title,(WIDTH//2 -title.get_width()//2,30))
    pygame.display.flip()

pygame.quit()
