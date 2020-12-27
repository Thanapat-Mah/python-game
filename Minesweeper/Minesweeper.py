import random
import pygame
from pygame.locals import *
#from CreateMatrix import createMatrix

pygame.init()

sw = 1600
sh = 900
matrixSpace = 60

win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Minesweeper")



class cell(object):
    def __init__(self, index):
        self.index = index
        self.num = 0
        self.bomb = False
        self.flag = False
        self.mark = False
        self.show = False



def createMatrix(row, col, bombNum):    
    #create initial matrix, swap between row and column
    cells = [[cell((j, i)) for i in range(col)] for j in range(row)]

    bombCount = 0
    bombIndex = []

    #define index of all bomb
    while bombCount < bombNum:
        i = random.randint(0, row-1)
        j = random.randint(0, col-1)
        if (i, j) not in bombIndex:
            bombIndex.append((i, j))
            bombCount += 1

    #function for count bomb in around
    def check_num(i, j):
        count = 0
        for m in range(i-1, i+2):
            for n in range(j-1, j+2):
                if (m, n) in bombIndex:
                    count += 1
        return count

    #generate data in matrix
    for i in range(row):
        for j in range(col):
            if (i, j) in bombIndex:
                cells[i][j].bomb = True
                #print("bomb", end = " ")
            else:
                cells[i][j].num = check_num(i, j)
                #print(cells[i][j].num, end = "    ")   
        #print("")
    return cells



row = 10
maxrow = 25
minrow = 2

col = 20
maxcol = 50
mincol = 2

bombNum = 30
maxbomb = int(round(row*col*0.3))
minbomb = 1

flagNum = 0
showCount = 0
time = 0
victory = False
gameOver = False

pygame.time.set_timer(USEREVENT+1, 1000)

cellSize = 30

cells = createMatrix(row, col, bombNum)

x1 = 140 + int(200*(col - mincol)/(maxcol - mincol))
x2 = 140 + int(200*(row - minrow)/(maxrow - minrow))
x3 = 140 + int(200*((bombNum - minbomb)/(maxbomb - minbomb)))



def createSetting(mousePos):
    global row, col, bombNum, x1, x2, x3, cells, flagNum, showCount, time, victory, gameOver
    
    colSet = int(round((x1 - 140)*(maxcol - mincol)/200 + mincol))
    rowSet = int(round((x2 - 140)*(maxrow - minrow)/200 + minrow))
    bombSet = int(round((x3 - 140)*(rowSet*colSet*0.3 - minbomb)/200 + minbomb))
    
    font = pygame.font.SysFont('comicsans', 30)
    
    #set width/col    
    if mousePos[0] >= 140 and mousePos[0] <= 140 + 200:
        if mousePos[1] >= 36 and mousePos[1] <= 44:
            if pygame.mouse.get_pressed()[0]:
                x1 = mousePos[0]
                
    pygame.draw.rect(win, (255, 255, 255), (140, 40, 200, 2))            
    pygame.draw.circle(win, (128, 255, 128), (x1, 40), 8)    
    
    width = font.render("Width : {}".format(str(colSet)), 1, (255, 255, 255))
    win.blit(width, (25, 30))
    
    

    #set height/row
    if mousePos[0] >= 140 and mousePos[0] <= 140 + 200:
        if mousePos[1] >= 56 and mousePos[1] <= 64:
            if pygame.mouse.get_pressed()[0]:
                x2 = mousePos[0]
                
    pygame.draw.rect(win, (255, 255, 255), (140, 60, 200, 2))
    pygame.draw.circle(win, (128, 255, 128), (x2, 60), 8)
    
    width = font.render("Height: {}".format(str(rowSet)), 1, (255, 255, 255))
    win.blit(width, (25, 50))


    
    #set bombNum
    if mousePos[0] >= 140 and mousePos[0] <= 140 + 200:
        if mousePos[1] >= 76 and mousePos[1] <= 84:
            if pygame.mouse.get_pressed()[0]:
                x3 = mousePos[0]
                
    pygame.draw.rect(win, (255, 255, 255), (140, 80, 200, 2))
    pygame.draw.circle(win, (128, 255, 128), (x3, 80), 8)
    
    width = font.render("Bombs: {}".format(str(bombSet)), 1, (255, 255, 255))
    win.blit(width, (25, 70))


    #New game confirm
    pygame.draw.rect(win, (255, 255, 255), (140, 95, 130, 25))
    text = font.render("New Game", 1, (0, 0, 255))
    win.blit(text, (150, 100))
    if mousePos[0] > 140 and mousePos[0] < 270:
        if mousePos[1] > 95 and mousePos[1] < 120:

            pygame.draw.rect(win, (255, 0, 0), (140, 95, 130, 25), 2)

            #create new game
            if pygame.mouse.get_pressed()[0]:
                col = colSet
                row = rowSet
                bombNum = bombSet
                #print("newGame click")
                font1 = pygame.font.SysFont('comicsans', 100)
                text = font1.render("Creating New Game...", 1, (255, 255, 255))
                win.blit(text, (int(sw - text.get_width())//2, int(sh - text.get_height())//2))
                pygame.display.update()
                cells = createMatrix(row, col, bombNum)
                flagNum = 0
                showCount = 0
                time = 0
                victory = False
                gameOver = False
                pygame.time.delay(1000)


    if mousePos[0] < 350 and mousePos[1] < 120:
        return True
    else:
        return False



def checkAround(i, j):
    global row, col, cells
    for m in range(i-1, i+2):
        for n in range(j-1, j+2):            
            if (m >= 0 and m < row) and (n >= 0 and n < col):                
                cell = cells[m][n]
                if not(cell.show) and not(cell.flag):
                    cell.show = True
                    if cell.num == 0:                        
                        checkAround(m, n)



def reveal(i, j):
    global row, col, cells
    flagCount = 0
    for m in range(i-1, i+2):
        for n in range(j-1, j+2):            
            if (m >= 0 and m < row) and (n >= 0 and n < col):                
                cell = cells[m][n]
                if cell.flag:
                    flagCount += 1
                    
    cell = cells[i][j]
    if flagCount == cell.num:
        for m in range(i-1, i+2):
            for n in range(j-1, j+2):
                if (m >= 0 and m < row) and (n >= 0 and n < col):                
                    cell = cells[m][n]
                    if not(cell.flag):
                        if cell.num == 0:
                            checkAround(m, n)
                        else:
                            cell.show = True



def fillCell(mousePos):
    global row, col, maxrow, maxcol, cells, cellSize, flagNum, showCount, matrixSpace, gameOver
    showCount = 0
    for i in range(row):
        for j in range(col):
            cell = cells[i][j]
            x = (sw-col*cellSize)//2 + j*cellSize
            y = (sh-row*cellSize)//2+matrixSpace + i*cellSize

            if gameOver:
                if cell.bomb:
                    pygame.draw.rect(win, (128, 0, 0), (x, y, cellSize, cellSize))
                elif cell.num != 0:
                    font = pygame.font.SysFont('comicsans', 40)
                    num = font.render(str(cell.num), 1, (0, 128, 0))
                    win.blit(num, (x+8, y+3))

                pygame.draw.rect(win, (0, 0, 128), (x, y, cellSize, cellSize), 1) #grid

                if cell.flag:
                    pygame.draw.rect(win, (255, 255, 0), (x+2, y+2, cellSize-4, cellSize-4), 4)
                
                if cell.show:
                    showCount += 1
                

            else:
                
                #cover unshow cell
                if not(cell.show):
                    pygame.draw.rect(win, (128, 128, 255), (x, y, cellSize, cellSize))

                    if cell.flag:
                        pygame.draw.rect(win, (255, 255, 0), (x, y, cellSize, cellSize))
                    elif cell.mark:
                        pygame.draw.rect(win, (200, 200, 128), (x, y, cellSize, cellSize))
                else:         
                    showCount += 1
                    
                    #show num
                    if cell.bomb:
                        gameOver = True
                    elif cell.num != 0:
                        font = pygame.font.SysFont('comicsans', 40)
                        num = font.render(str(cell.num), 1, (0, 128, 0))
                        win.blit(num, (x+8, y+3))

                pygame.draw.rect(win, (0, 0, 128), (x, y, cellSize, cellSize), 1) #grid
                
                #mouse tracking
                #mousePos = pygame.mouse.get_pos()
                if mousePos[0] - x > 0 and mousePos[0] - x  < cellSize:
                    if mousePos[1] - y > 0 and mousePos[1] - y < cellSize:
                        pygame.draw.rect(win, (255, 0, 0), (x, y, cellSize, cellSize), 2) #highlight
                        if pygame.mouse.get_pressed()[0]: #left mouse click
                            if cell.bomb and not(cell.flag):
                                gameOver = True
                            elif not(cell.show) and cell.num != 0:
                                cell.show = True
                                pygame.time.delay(300)
                                #print("show num")
                            elif cell.num == 0:
                                checkAround(i, j)
                                #print("checkAroud")
                            elif cell.num != 0:
                                reveal(i, j)
                                #print("reveal")
                            else:
                                cell.show = True
                            pygame.time.delay(10)
                        elif pygame.mouse.get_pressed()[2] and not(cell.show): #right mouse click
                            if not(cell.flag) and not(cell.mark):
                                cell.flag = True
                                cell.mark = False
                                flagNum += 1
                                #print("flag")
                            elif cell.flag and not(cell.mark):
                                cell.flag = False
                                cell.mark = True
                                flagNum -= 1
                                #print("mark")
                            elif not(cell.flag) and cell.mark:
                                cell.flag = False
                                cell.mark = False
                                #print("unmark")
                            pygame.time.delay(int(120 - 100*row*col/(maxrow*maxcol)))



def scoreBoard():
    global sw, sh, row, col, bombNum, flagNum, showCount, time, victory
    pygame.draw.rect(win, (255, 255, 255), ((sw - 600)//2, 25, 600, 100), 3) #frame

    font = pygame.font.SysFont('comicsans', 70)
    font2 = pygame.font.SysFont('comicsans', 30)
    red = (255, 64, 64)
    white = (255, 255, 255)

    text = font.render(str(flagNum) + "/" + str(bombNum), 1, red)
    textHead = font2.render("Flag/Bomb", 1, white)
    win.blit(textHead, (int(sw - textHead.get_width())//2 - 200, 40))
    win.blit(text, (int(sw - text.get_width())//2 - 200, 70))

    text2 = font.render(str(showCount) + "/" + str(row*col - bombNum), 1, red)
    textHead2 = font2.render("Showed", 1, white)
    win.blit(textHead2, (int(sw - textHead2.get_width())//2 + 30, 40))
    win.blit(text2, (int(sw - text2.get_width())//2 + 30, 70))
    
    clock = font.render(str(time), 1, red)
    clockHead = font2.render("Time", 1, white)
    win.blit(clockHead, (int(sw - clockHead.get_width())//2 + 200 + 30, 40))
    win.blit(clock, (int(sw - clock.get_width())//2 + 200 +30, 70))

    if showCount == row*col - bombNum: #flagNum == bombNum and 
        victory = True



def redrawGameWindow(mousePos):
    win.fill((0, 0, 0)) #fill background color
    global cells, row, col, bombNum, matrixSpace, victory, gameOver
    
    if not(createSetting(mousePos)):        
        pygame.draw.rect(win, (200, 200, 200), ((sw-col*cellSize)//2, (sh-row*cellSize)//2+matrixSpace, col*30, row*30)) #matrix's background
        fillCell(mousePos)
        pygame.draw.rect(win, (255, 255, 255), ((sw-col*cellSize)//2, (sh-row*cellSize)//2+matrixSpace, col*30, row*30), 3) #matrix's frame  

    else:
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render("Game Setting...", 1, (255, 255, 255))
        win.blit(text, (int(sw - text.get_width())//2, int(sh - text.get_height())//2))
        
    scoreBoard()
    
    if victory:
        font = pygame.font.SysFont('comicsans', 70)
        text = font.render("VICTORY", 1, (255, 255, 255))
        win.blit(text, (int(sw - text.get_width())//2 + 480, 50))

    elif gameOver:
        font = pygame.font.SysFont('comicsans', 70)
        text = font.render("GAME OVER", 1, (255, 255, 255))
        win.blit(text, (int(sw - text.get_width())//2 + 480, 50))
    
    pygame.display.update()



#mainloop
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == USEREVENT+1 and not(victory) and not(gameOver):
            time += 1 
    
    mousePos = pygame.mouse.get_pos()

    redrawGameWindow(mousePos)
    
pygame.quit()
