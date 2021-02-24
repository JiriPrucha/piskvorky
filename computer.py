import random

newTick = []

class Board:
    def __init__(self, rank, tick):
        self.tick = tick
        self.rank = rank

    def update(self, rank, tick):
        self.rank = rank
        self.tick = tick
rowCount = 15

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

def main(x,y):

def ai(board):
    player = [[0,0,0],[0,0,0],[0,0,0]]
    ai = [[0,0,0],[0,0,0],[0,0,0]]
    playerSymbolsOfTurns = [[0,0,0],[0,0,0],[0,0,0]]
    aiSymbolsOfTurns = [[0,0,0],[0,0,0],[0,0,0]]

    if newTick != []:
        player, playerSymbolsOfTurns = possibleTurns(board,xp,yp,1)
    if xai != 150:
        ai, aiSymbolsOfTurns = possibleTurns(board,xai,yai,2)

    x,y = bestTurn(player,ai, playerSymbolsOfTurns, aiSymbolsOfTurns, xp, yp, xai, yai)

    return x, y

def possibleTurns(board,xp,yp, sym):
    scoreOfTurns = [[0,0,0],[0,0,0],[0,0,0]]
    symbolsOfTurns = [[0,0,0],[0,0,0],[0,0,0]]

    x = 1
    y = 1

    if xp != len(board):
        if yp != len(board):
            scoreOfTurns[x+1][y+1], symbolsOfTurns[x+1][y+1] = score(board, xp+1, yp+1, sym)
        scoreOfTurns[x+1][y], symbolsOfTurns[x+1][y] = score(board, xp+1, yp, sym)
        if yp != 0:
            scoreOfTurns[x+1][y-1],symbolsOfTurns[x+1][y-1] = score(board, xp+1, yp-1, sym)
    if xp != 0:
        if yp != 0:
            scoreOfTurns[x][y-1],symbolsOfTurns[x][y-1] = score(board, xp, yp-1, sym)
        scoreOfTurns[x-1][y-1],symbolsOfTurns[x-1][y-1] = score(board, xp-1, yp-1, sym)
        if yp != len(board):
            scoreOfTurns[x-1][y],symbolsOfTurns[x-1][y] = score(board, xp-1, yp, sym)
    if yp != 0:
        scoreOfTurns[x-1][y+1],symbolsOfTurns[x-1][y+1] = score(board, xp-1, yp+1, sym)
    if yp != len(board):
        scoreOfTurns[x][y+1],symbolsOfTurns[x][y+1] = score(board, xp, yp+1, sym)

    return scoreOfTurns, symbolsOfTurns


def score(board, x, y, sym):
    scoreOfPlace = 0
    symbol = board[x][y]

    scoreOfPlace += coJaVim(board,x + 1,y + 1,0, 0, sym)
    scoreOfPlace += coJaVim(board,x + 1,y,1, 0, sym)
    scoreOfPlace += coJaVim(board,x + 1,y - 1,2, 0, sym)
    scoreOfPlace += coJaVim(board,x,y - 1,3, 0, sym)
    scoreOfPlace += coJaVim(board,x - 1,y - 1,4, 0, sym)
    scoreOfPlace += coJaVim(board,x - 1,y,5, 0, sym)
    scoreOfPlace += coJaVim(board,x - 1,y + 1,6, 0, sym)
    scoreOfPlace += coJaVim(board,x,y + 1,7, 0, sym)

    return scoreOfPlace, symbol

def coJaVim(board,x,y,controll, cycle, sym):
    cycle += 1
    score, sym = boardRead(board, x, y, sym)
    if sym == board[x][y]:
        if controll == 0:
            x += 1
            y += 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
        elif controll == 1:
            x += 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
        elif controll == 2:
            x += 1
            y -= 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
        elif controll == 3:
            y -= 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
        elif controll == 4:
            x -= 1
            y -= 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
        elif controll == 5:
            x -= 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
        elif controll == 6:
            x -= 1
            y += 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
        else:
            y += 1
            return coJaVim(board,x,y,controll, cycle + 1, sym)
    elif score == 10 and sym != board[x][y]:
        score = finalScore(cycle, score)
    else:
        score = finalScore(cycle, 0)
    return score

def finalScore(cycle, sym):
    score = 0
    if sym == 10 and cycle == 1:
        return sym
    else:
        score = (cycle-1) * 10 - int(sym/2)
        for i in range(1, cycle - 1):
            score += (i * 10)
        return score

def boardRead(board, x, y, sym):
    secondSym = (sym + 1)//2

    if board[x][y] == sym:
        return 10, sym
    elif board[x][y] == secondSym:
        return 10, secondSym
    else:
        return 0, 2 

def bestTurn(pos1, pos2, playerSOT,aiSOT, xp,yp, xai,yai):
    turn1 = 0
    turn2 = 0

    if xp != 150:
        con = False
        while con == False:
            turn1, x1, y1 = maximumScore(pos1)
            if playerSOT[x1][y1] == 0:
                con = True
            else:
                pos1[x1][y1] = 0
    if xai != 150:
        con = False
        while con == False:
            turn2, x2, y2 = maximumScore(pos2)
            if aiSOT[x2][y2] == 0:
                con = True
            else:
                pos2[x2][y2] = 0
    
    if turn2 > turn1:
        x = realXY(x2,xai)
        y = realXY(y2,yai)
        return x,y
    else:
        x = realXY(x1,xp)
        y = realXY(y1,yp)
        return x,y

def maximumScore(pos):
    xMaxScore = []
    yMaxScore =  []
    maxScore = -100
    for i in range(3):
        for j in range(3):
            if pos[j][i] > maxScore:
                maxScore = pos[j][i]
                xMaxScore = []
                yMaxScore = []
                xMaxScore.append(j)
                yMaxScore.append(i)
            elif pos[j][i] == maxScore:
                xMaxScore.append(j)
                yMaxScore.append(i)
    if len(xMaxScore) > 1:
        k = random.randint(0,len(xMaxScore))
        return maxScore, xMaxScore[k], yMaxScore[k]
    else:
        return maxScore,xMaxScore[0],yMaxScore[0]

def realXY(x,xp):
    if x == 0:
        return (xp - 1)
    elif x == 1:
        return xp
    else:
        return (xp + 1)