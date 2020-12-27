import pygame

pygame.init()

win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Minesweeper")

def redrawGameWindow():
    win.fill((0, 0, 0))
    
    pygame.draw.rect(win, (128, 128, 128), ((1600-20*30)//2, (900-10*30)//2+60, 20*30, 10*30))
    pygame.draw.rect(win, (255, 255, 255), ((1600-20*30)//2, (9000-10*30)//2+60, 20*30, 10*30), 3)
    
    pygame.display.update()

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()
    
pygame.quit()
