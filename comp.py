"""
Piškvorky
Jiří Průcha, I. ročník
Zimní semestr 2020/2021
Programování I

"""

import turns

"""
PROMĚNNÉ:
(některé proměnné jsou popsané v dalších souborech)

newTick - list, do kterého se ukládají obsazené pozice. Tedy pozice, na kterých je umístěný nějaký kamen.
field - list, přes který vstupuji do třídy Board
twoInARow - *********************************************************************************************
positions - Do tohoto listu se ukládají pozice, které se v tomto tahu ohodnotili. Tedy možné další tahy.
nextTurn = zásobník, do kterého se ukládají příští tahy. Tento zásobník se využívá pokud se nalezne možnost jak dobře hrát několik tahů dopředu.

Board:
    rankX, rankO - hodnocení pozice pro Xka respektive pro Očka. Do těchto proměnných se ukládá skóre této pozic.
    tick - Druh kamene. 1 pro X nebo 2 pro O. To samé platí i mimo Board. Tedy jako normální proměnná

neighbors - Počet sousedů, na které se nedá umístit kámen.

j - určuje, jakým směrem hledáme. Podle ukázky pod tímto řádkem je vidět, s jakým číslem se hledá kde

    5 4 3
    6 + 2
    7 8 1

numberOfTwo - Proměnná, do které se ukládá počet míst, na které se po vložení kamene vytvoří trojice
countOfScore - Pokud se na jedné pozici nachází stejné nejvyšší score vícekrát, pak se do této proměnné ukládá počet.

a,b = x,y po zavolání některých funkcí

number - [0] počet nul v okolí. [1] počet X/O v okolí. Podle toho, co je zrovna naše priorita. [2] počet soupeřů v okolí. [3] Pokud se 
"""
newTick = []
field =  []
twoInARow = []

positions = []

nextTurn = []

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

def createBoard(rowCount):
    for _ in range(rowCount):
            field.append([])
    for y in range(rowCount):
        for _ in range(rowCount):
            field[y].append(Board(0,0,0))


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

# Hledá možné tahy kolem pozice, kteru mu zadáme
def possibleTurns(x,y,i):
    numberOfTwo = 0
    neighbors = 0
    if x != len(field)-1 and y != len(field)-1 and field[x+1][y+1].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x+1][y+1].updateX(turn(x+1, y+1, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x+1][y+1].updateO(turn(x+1, y+1, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if x != len(field)-1 and field[x+1][y].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x+1][y].updateX(turn(x+1, y, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x+1][y].updateO(turn(x+1, y, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if x != len(field)-1 and y != 0 and field[x+1][y-1].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x+1][y-1].updateX(turn(x+1, y-1, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x+1][y-1].updateO(turn(x+1, y-1, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if y != 0 and field[x][y-1].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x][y-1].updateX(turn(x, y-1, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x][y-1].updateO(turn(x, y-1, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if x != 0 and y != 0 and field[x-1][y-1].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x-1][y-1].updateX(turn(x-1, y-1, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x-1][y-1].updateO(turn(x-1, y-1, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if x != 0 and field[x-1][y].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x-1][y].updateX(turn(x-1, y, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x-1][y].updateO(turn(x-1, y, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if x != 0 and y != len(field)-1 and field[x-1][y+1].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x-1][y+1].updateX(turn(x-1, y+1, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x-1][y+1].updateO(turn(x-1, y+1, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if y != len(field)-1 and field[x][y+1].tick == 0:
        numberOfTwo = len(twoInARow)
        field[x][y+1].updateX(turn(x, y+1, 1))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,1])
            numberOfTwo = len(twoInARow)
        field[x][y+1].updateO(turn(x, y+1, 2))
        if len(twoInARow) > numberOfTwo:
            twoInARow.append([x,y,2])
    else:
        neighbors += 1
    if neighbors == 8:
        newTick.pop(i)

# Kontroluje, zda se na této pozici nevyskytuje již nějaký další kamen
def turn(x, y, tick):
    if tick == 1 and field[x][y].rankX == 0:
        positions.append([x,y])
        return toWhichSide(x,y,tick)
    elif tick == 2 and field[x][y].rankO == 0:
        return toWhichSide(x,y,tick)
    elif tick == 1:
        return field[x][y].rankX
    else:
        return field[x][y].rankO

# Tato fuknce vyhodnotí nejvyšší možné score, které lze na určené pozici udělat. Určité skóre se zde i násobí. A to jen ty, u kterých je to poté 99% váhra
def toWhichSide(x,y,tick):
    listOfScore = []
    countOfScore = 0
    for i in range(4):
        number = choosingPlace(x,y,tick,i+1)
        listOfScore.append(scoreOfTile(number))

    score = max(listOfScore)
    
    if score == 72000 or score == 60000 or score == 40000:
        for whatScore in listOfScore:
            if whatScore == score:
                countOfScore += 1
        score *= countOfScore
    if score == 40000:
        twoInARow.append([x,y])
    return score
         
# Podle listu number se zde vytváří skore pro tuto pozici a tento směr
def scoreOfTile(number):
    if number[1] == 4 and number[3] == 0:
        return 200000
    elif number[1] == 4:
        return 150000
    elif number[1] == 3 and number[2] == 0 and number[3] == 0:
        return 72000
    elif number[1] == 3 and number[2] == 0 and number[3] == 1:
        return 60000
    elif number[1] == 2 and number[2] == 0 and number[3] == 0:
        return 40000
    else:
        score = number[1] - number[2]
        score = (score ** number[1])
        if number[0] == 4 and number[1] != 0 and number[2] == 0:
            score += 10
        else:
            score += (number[0] * 2)
        if number[3] != 0:
            score - 20
        return score


def whatIsThere(tick,i,j,promenna,number, numberFinal):
    if promenna == 0:
        if number[0] == 0 and number[1] != 0:
            number[5] += 1
        elif number[0] == 1 and number[1] != 0 and number[5] > 1:
            number[5] -= 1
            i += 1
        else:
            i += 1
        number[0] += 1
        numberFinal[0] += 1
    elif promenna == tick:
        if number[5] == 1:
            number[3] +=1
            numberFinal[3] += 1
        if number[4] == 2 and number[0] == 1 and number[1] == 0 and number[2] == 0:
            number[3] +=1
            numberFinal[3] += 1
        number[1] += 1
        numberFinal[1] += 1
        i = 1
        j += 1
    else:
        if number[0] == 1 and number[1] != 0 and number[3] > 2:
            number[5] -= 1
        else:
            number[2] += 1
            numberFinal[2] += 1
        i = 2

    return i, j, number, numberFinal

# Kontroluje, okolí kolem pozice v předem určeném směru. Používá k tomu dva while cikly. V nich postupě volá funkci whatIsThere(), až dokud se některá z podmínek nenaplní. Nakonec vrátí čísla, ze kterých se bude počítat score
def choosingPlace(a,b,tick,j):
    cross = 0
    circle = 0
    nothing = 0
    numberFinal = [0,0,0,0]
    number = [0,0,0,0,0,0]

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
            nothing, cross, number, numberFinal = whatIsThere(tick,nothing, cross,field[x][y].tick, number, numberFinal)
            isPossible,x,y = switch(x,y,j)
        j += 4
        number = [0,0,0,0,0,0]
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


# Vyhledá nejlepší možný tah. Pokud je nejlepší možný tah vytvoření trojice, pak se to pokusí vytvořit několik tahů dopředu tak, aby se nakonec dosáhlo vytvoření dvou trojic najednou. Což zaručuje výhru
def bestTurn():
    x = 0
    y = 0
    maximumX = 0
    maximumO = 0
    game_over = False
    tryAgain = True
    cont = 0

    if positions == []:
        return 150, 150, True

    for coordinates in positions:
        i,j = coordinates[0],coordinates[1]
        if field[i][j].rankO > maximumO:
            maximumO = field[i][j].rankO
            maximumX = field[i][j].rankX
            x, y = i, j

            if maximumO == 200000:
                game_over = True

        elif field[i][j].rankO == maximumO:
            if field[i][j].rankX > maximumX:
                maximumX = field[i][j].rankX
                x, y = i, j

    for coordinates in positions:
        i,j = coordinates[0],coordinates[1]

        if field[i][j].rankX > maximumO and (field[i][j].rankX > 40000 or  maximumO < 1000):
            maximumO = field[i][j].rankX
            maximumX = field[i][j].rankO
            x, y = i, j

    if maximumO < 41000 and nextTurn != []:
        box = nextTurn.pop(-1)
        x,y = box[0],box[1]

    elif maximumO == 40000 and cont == 0:
        cont += 1
        ifTrue,lifo = turns.ifThreeIsPossible()
        if ifTrue:
            for i in range(len(lifo)):
                nextTurn.append(lifo[i])

            box = nextTurn.pop(-1)
            x,y = box[0], box[1]

    for coordinates in positions:
        i,j = coordinates[0],coordinates[1]
        field[i][j].rankX, field[i][j].rankO = 0,0
    coordinates = []
    return x,y,game_over

# Hlavní část tohoto souboru. Řídí zbytek funkcí
def main():
    for _ in range(len(twoInARow)):
        twoInARow.pop(-1)

    game_over = False
    i = 0
    cont = True
    if newTick == [] and field[len(field)//2][len(field)//2].tick == 0:
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