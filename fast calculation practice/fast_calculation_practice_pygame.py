import pygame
from pygame.locals import *
import random

pygame.init()
sw = 1600
sh = 900
win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Fast Calculation Practice")

start = True
rounds = 0



class data(object):
    def __init__(self):
        self.question = []
        self.answer = 0
        self.log = ""
        time = 0

       

def generateQuestion():
    global rounds

    #set initial values
    dataWork = data()    
    amount = 0    
    ans = 0

    #calculation buffer
    callist = []
    num1 = 0
    num2 = 0
    op_rand = False
    op = 0
    oplist = ["+", "-", "*", "/"]
    log = "" #calculation log
    
    #check round, set amount of number
    if(((rounds-1)//5)%2 == 0): amount = 4
    else: amount = 5
    
    #random number
    for i in range(amount): dataWork.question.append(random.randint(1, 9))
    callist = dataWork.question.copy()
    print("{} callist = {}".format(rounds, callist))####
            
    #calculate
    for i in range(amount - 1):
        #random pair of number
        num1 = int(callist.pop(random.randint(0, (len(callist) - 1) )))
        num2 = int(callist.pop(random.randint(0, (len(callist) - 1) )))
        op_rand = True
        
        #random operation & calculate
        while op_rand:
            op = random.randint(0, 3)
            if(op == 0): ans = num1 + num2
            elif(op == 1): ans = num1 - num2
            elif(op == 2): ans = num1 * num2
            else:
                if(num2 != 0): ans = num1 / num2
                            
            if((ans%1 == 0) and (ans >= 0) and (num2 != 0)):
                callist.append(ans)
                op_rand = False
                
                #calculation log
                log = log + str(num1) + oplist[op] + str(num2)
                if(len(callist) > 1): log += ", "
    
    #output
    dataWork.answer = int(ans)
    dataWork.log = log

    return dataWork


pygame.time.set_timer(USEREVENT+1, 1000)
time = 0
showSol = False
dataWork = data()
dataWork.question = [0, 0, 0, 0]
dataWork.answer = "Goal"
dataWork.log = "This is solution"
def control():
    global rounds, time, showSol, noCount, dataWork
    smallFont = pygame.font.SysFont("comicsans", 30)
    midFont = pygame.font.SysFont("comicsans", 60)
    bigFont = pygame.font.SysFont("comicsans", 120)

    #no. & clock
    pygame.draw.rect(win, (0, 0, 255), ((sw-400)//2, 40, 400, 100), 2)
    label = smallFont.render("No.", 1, (128, 128, 128))
    win.blit(label, ((sw - label.get_width())//2 - 100, 55))
    num = midFont.render(str(rounds), 1, (255, 0, 0))
    win.blit(num, ((sw - num.get_width())//2 - 100, 90))

    label2 = smallFont.render("Time", 1, (128, 128, 128))
    win.blit(label2, ((sw - label2.get_width())//2 + 100, 55))
    clock = midFont.render(str(time), 1, (255, 0, 0))
    win.blit(clock, ((sw - clock.get_width())//2 + 100, 90))


    #question num
    for i in range(len(dataWork.question)):
        pygame.draw.rect(win, (128, 0, 128), ((sw-150)//2 - 100*len(dataWork.question) + 250*i, 220, 150, 180))
        questNum = bigFont.render(str(dataWork.question[i]), 1, (255, 255, 255))
        win.blit(questNum, ((sw-questNum.get_width())//2 - 100*len(dataWork.question) + 250*i, 270))


    #question answer
    pygame.draw.rect(win, (128, 128, 255), ((sw-300)//2, 470, 300, 120))
    ans = bigFont.render(str(dataWork.answer), 1, (255, 255, 255))
    win.blit(ans, ((sw - ans.get_width())//2, 490))


    #start button
    mousePos = pygame.mouse.get_pos()
    
    pygame.draw.rect(win, (0, 255, 0), ((sw-200)//2 + 400, 490, 200, 80))
    text = midFont.render("Next", 1, (255, 255, 255))
    win.blit(text, ((sw - text.get_width())//2 + 400, 510))

    if mousePos[0] > (sw-200)//2+400 and mousePos[0] < (sw-200)//2 + 600:
        if mousePos[1] > 490 and mousePos[1] < 570:
            pygame.draw.rect(win, (255, 0, 0), ((sw-200)//2 + 400, 490, 200, 80), 3) #highlight
            if pygame.mouse.get_pressed()[0]:
                rounds += 1
                showSol = False
                dataWork = generateQuestion()
                time = 0
                pygame.time.delay(500)

    #show solution button
    pygame.draw.rect(win, (255, 128, 64), ((sw-200)//2, 620, 200, 40))
    text2 = smallFont.render("Show solution", 1, (255, 255, 255))
    win.blit(text2, ((sw - text2.get_width())//2, 630))
    
    if mousePos[0] > (sw-200)//2 and mousePos[0] < (sw-200)//2 + 200:
        if mousePos[1] > 620 and mousePos[1] < 660:
            pygame.draw.rect(win, (255, 0, 0), ((sw-200)//2, 620, 200, 40), 3) #highlight
            if pygame.mouse.get_pressed()[0]:
                showSol = True

    if showSol:
        solution = midFont.render(dataWork.log, 1, (0, 0, 0))
        win.blit(solution, ((sw - solution.get_width())//2, 750))
        



def redrawWindow():
    win.fill((255, 255, 255))
    control()
    pygame.display.update()




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == USEREVENT+1:
            time += 1

    redrawWindow()

pygame.quit()
