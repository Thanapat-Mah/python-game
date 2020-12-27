import random

class cell(object):
    def __init__(self, index):
        self.index = index
        #self.pos = (0, 0)
        self.mouse = False
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
                print("bomb", end = " ")
            else:
                cells[i][j].num = check_num(i, j)
                print(cells[i][j].num, end = "    ")   
        print("")
    return cells   


