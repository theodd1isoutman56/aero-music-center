import pygame
import sys
WIDTH = 1000
HEIGHT = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
caption = pygame.display.set_caption('AERO MUSIC CENTER')
BG = pygame.image.load('fruitiger1.webp').convert_alpha()
BG_RECT = BG.get_rect(center =(500,300))
time = pygame.time.Clock()
running = True
pygame.font.init()
font_main = pygame.font.SysFont('Arial', 45, bold = True)
font_sub = pygame.font.SysFont('Arial', 50, bold = True)
font_sub_2 = pygame.font.SysFont('Arial', 35, bold = True)
font_heading = pygame.font.SysFont('Arial', 30, bold = True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((74, 201, 227))
    screen.blit(BG,BG_RECT)
    title = font_main.render('AERO MUSIC ',True , (5, 185, 230))
    screen.blit(title,(WIDTH//2 -title.get_width()//2,30))
    title_below = font_main.render('CENTRE ',True , (99, 196, 142))
    screen.blit(title_below,(WIDTH//2 -title_below.get_width()//2,100))
    title_2 = font_heading.render('Welcome , which song are u picking first?',True , (255,255,255))
    screen.blit(title_2,(20,150))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
