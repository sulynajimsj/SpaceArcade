import pygame
import sys


pygame.init()
res = (700, 700)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()

# defining a font
bigfont = pygame.font.SysFont('Anima', 70)
smallfont = pygame.font.SysFont('Segoe UI', 25)
smallerfont = pygame.font.SysFont('Segoe UI', 10)
text = smallfont.render('Left Arrow for Space Invader', True, (250,250,250))
text2 = smallfont.render('Right Arrow for Space PVP (NEW!)', True, (250,250,250))
textesc = smallerfont.render('Start with Left game (Space Invader) to avoid a crash', True, (250,250,250))
textesc2 = smallerfont.render('Esc to return to menu and close tabs for best experience :)', True, (250,250,250))

text3 = bigfont.render("Space Arcade", True, (250,250,250))


while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                exec(open('main.py').read())
            if event.key == pygame.K_RIGHT:
                exec(open('main2.py').read())
        if event.type == pygame.QUIT:
            pygame.quit()



    screen.fill((60, 25, 60))
    screen.blit(text, (200, height / 2 - 100))
    screen.blit(text2, (200, height / 2+100))
    screen.blit(text3, (200, 50))
    screen.blit(textesc, (210, height/2 + 250))
    screen.blit(textesc2, (210, height/2 + 280))
    pygame.display.update()
