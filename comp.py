newTick = []
field =  []

class Board:
    def __init__(self, rankX, rankO, tick):
        self.rankX = rankX
        self.rankO = rankO
        self.tick = tick

    def updateTick(self, tick):
        self.tick = tick

    def updateO(self, rankO):
        self.rankO = rankO
    
    def updateX(self, rankX):
        self.rankX = rankX

field = [[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)],
[Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0),Board(0,0,0)]
]

def createBoard(rowCount):
    """
    for _ in range(rowCount):
            field.append([])
    for y in range(rowCount):
        for _ in range(rowCount):
            field[y].append(Board(0,0,0))
"""
    pass

def switch(x,y,j):
    if j == 1:
        return one(x,y)
    elif j == 2:
        return two(x,y)
    elif j == 3:
        return three(x,y)
    elif j == 4:
        return four(x,y)
    elif j == 5:
        return five(x,y)
    elif j == 6:
        return six(x,y)
    elif j == 7:
        return seven(x,y)
    else:
        return eight(x,y)

def one(x,y):
    if x != (len(field)-1) and y != (len(field)-1):
	    return True,x+1,y+1
    else:
        return False ,x,y
def two(x,y):
    if x != (len(field)-1):
	    return True,x+1,y
    else:
        return False,x,y
def three(x,y):
    if x != (len(field)-1) and y != 0:
	    return True,x+1,y-1
    else:
        return False,x,y
def four(x,y):
    if y != 0:
	    return True,x,y-1
    else:
        return False,x,y
def five(x,y):
    if x != 0 and y != 0:
	    return True,x-1,y-1
    else:
        return False,x,y
def six(x,y):
    if x != 0:
	    return True,x-1,y
    else:
        return False,x,y
def seven(x,y):
    if x != 0 and y != (len(field)-1):
	    return True,x-1,y+1
    else:
        return False,x,y
def eight(x,y):
    if y != (len(field)-1):
	    return True,x,y+1
    else:
        return False,x,y

def possibleTurns(x,y,i):
    neighbors = 0
    if x != len(field)-1 and y != len(field)-1 and field[x+1][y+1].tick == 0:
        field[x+1][y+1].updateX(turn(x+1, y+1, 1))
        field[x+1][y+1].updateO(turn(x+1, y+1, 2)) 
    else:
        neighbors += 1
    if x != len(field)-1 and field[x+1][y].tick == 0:
        field[x+1][y].updateX(turn(x+1, y, 1))
        field[x+1][y].updateO(turn(x+1, y, 2))
    else:
        neighbors += 1
    if x != len(field)-1 and y != 0 and field[x+1][y-1].tick == 0:
        field[x+1][y-1].updateX(turn(x+1, y-1, 1))
        field[x+1][y-1].updateO(turn(x+1, y-1, 2))
    else:
        neighbors += 1
    if y != 0 and field[x][y-1].tick == 0:
        field[x][y-1].updateX(turn(x, y-1, 1))
        field[x][y-1].updateO(turn(x, y-1, 2))
    else:
        neighbors += 1
    if x != 0 and y != 0 and field[x-1][y-1].tick == 0:
        field[x-1][y-1].updateX(turn(x-1, y-1, 1))
        field[x-1][y-1].updateO(turn(x-1, y-1, 2))
    else:
        neighbors += 1
    if x != 0 and field[x-1][y].tick == 0:
        field[x-1][y].updateX(turn(x-1, y, 1))
        field[x-1][y].updateO(turn(x-1, y, 2))
    else:
        neighbors += 1
    if x != 0 and y != len(field)-1 and field[x-1][y+1].tick == 0:
        field[x-1][y+1].updateX(turn(x-1, y+1, 1))
        field[x-1][y+1].updateO(turn(x-1, y+1, 2))
    else:
        neighbors += 1
    if y != len(field)-1 and field[x][y+1].tick == 0:
        field[x][y+1].updateX(turn(x, y+1, 1))
        field[x][y+1].updateO(turn(x, y+1, 2))
    else:
        neighbors += 1
    if neighbors == 8:
        newTick.pop(i)

def turn(x, y, k):
    if k == 1 and field[x][y].rankX == 0:
        return pomoc(x,y,k)
    elif k == 2 and field[x][y].rankO == 0:
        return pomoc(x,y,k)
    elif k == 1:
        return field[x][y].rankX
    else:
        return field[x][y].rankO

def pomoc(x,y,k):
    listOfScore = []
    count = 0
    for i in range(4):
        number = choosingPlace(x,y,k,i+1)
        listOfScore.append(scoreOfTile(number))

    score = max(listOfScore)
    
    if score == 90000 or score == 40000:
        for whatScore in listOfScore:
            if whatScore == score:
                count += 1
        score *= count

    return score
         
def scoreOfTile(number):
    if number[1] == 4 and number[3] == 0:
        return 200000
    elif number[1] == 4:
        return 100000
    elif number[1] == 3 and number[2] == 0 and number[3] == 0:
        return 90000
    elif number[1] == 3 and number[2] == 0 and number[3] == 1:
        return 85000
    elif number[1] == 2 and number[2] == 0 and number[3] == 0:
        return 40000
    else:
        score = number[1] - number[2]
        score = (score ** number[1])
        if number[0] == 4 and number[1] != 0 and number[2] == 0:
            score -= 10
        else:
            score += (number[0] * 2)
        if number[3] != 0:
            score - 20
        return score

def whatIsThere(k,i,j,promenna,number, numberFinal):
    if promenna == 0:
        if number[0] == 0 and number[1] != 0:
            number[3] += 3
            numberFinal[3] += 3
        elif number[0] == 1 and number[1] != 0 and number[3] > 2:
            number[3] -= 3
            numberFinal[3] -= 3
        else:
            i += 1
        number[0] += 1
        numberFinal[0] += 1
    elif promenna == k:
        if number[4] == 2 and number[0] == 1 and number[1] == 0 and number[2] == 0:
            number[3] +=1
            numberFinal[3] += 1
        number[1] += 1
        numberFinal[1] += 1
        i = 1
        j += 1
    else:
        if number[0] == 1 and number[1] != 0 and number[3] > 2:
            number[3] -= 3
            numberFinal[3] -= 3
        else:
            number[2] += 1
            numberFinal[2] += 1
        i = 2

    return i, j, number, numberFinal

def choosingPlace(a,b,k,j):
    cross = 0
    circle = 0
    nothing = 0
    numberFinal = [0,0,0,0]
    number = [0,0,0,0,0]

    isPossible = True
    isPossible,x,y = switch(a,b,j)
    if isPossible == False:
        j += 4
        circle += 1
        x,y = a,b
        isPossible,x,y = switch(a,b,j)
        if isPossible == True:
            numberFinal[2] += 1

    while isPossible and cross != 4 and circle != 2:
        while nothing != 2 and isPossible and cross != 4:
            number[4] += 1
            nothing, cross, number, numberFinal = whatIsThere(k,nothing, cross,field[x][y].tick, number, numberFinal)
            isPossible,x,y = switch(x,y,j)
        j += 4
        number = [0,0,0,0,0]
        circle += 1
        nothing = 0
        x,y = a,b
        if isPossible == False:
            isPossible,x,y = switch(a,b,j)
            if isPossible == True:
                numberFinal[2] += 1
        else:
            isPossible,x,y = switch(x,y,j)

    return numberFinal

def bestTurn():
    x = 0
    y = 0
    maximumX = 0
    maximumO = 0
    game_over = False


    for j in range (len(field)):
        for i in range (len(field)):
            print("o = ",field[i][j].rankO)
            print("x = ",field[i][j].rankX)
            if field[i][j].rankO > maximumO:
                maximumO = field[i][j].rankO
                maximumX = field[i][j].rankX
                x, y = i, j
                print("max")

                if maximumO == 200000:
                    game_over = True

            elif field[i][j].rankO == maximumO:
                if field[i][j].rankX > maximumX:
                    maximumX = field[i][j].rankX
                    x, y = i, j
                    print("max")

    for j in range (len(field)):
        for i in range (len(field)):

            if field[i][j].rankX > maximumO and field[i][j].rankX > 40000:
                maximumO = field[i][j].rankX
                maximumX = field[i][j].rankX
                x, y = i, j
                print("max")

            field[i][j].rankX, field[i][j].rankO = 0,0
    print("------------------------------------------------------------")
    return x,y,game_over

def main():
    game_over = False
    i = 0
    cont = True
    if newTick == []:
        return len(field)//2,len(field)//2,game_over
    else:
        while cont:
            lenghtBefore = len(newTick)
            if i == lenghtBefore:
                cont = False
            else:
                x, y = newTick[i][0], newTick[i][1]
                possibleTurns(x,y,i)
                lenghtAfter = len(newTick)
                if lenghtBefore == lenghtAfter:
                    i += 1

    x,y,game_over = bestTurn()
    return x,y,game_over