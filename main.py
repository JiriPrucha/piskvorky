import sys
import os
import random
import pygame
from pygame import Rect, Vector2, Color

import comp

#Screen
width = 1000
height = 750

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255, 0, 255)

#Potřebné proměnné
rowCount = 15

player = 0
ai = 1                  #For two players to play against each other there is need for this value to be changed to 2 or more.

emptyPiece = 0
playerPiece = 1
aiPiece = 2

squareSize = 38
gap = 2
battlefieldSize = (squareSize * rowCount + (rowCount + 1) * gap)

game_over = False

squareWidth = int((width - battlefieldSize)/2)
squareHeight = int((height - battlefieldSize)/2)

def fix_path(p):
    return os.path.dirname(os.path.realpath(__file__)) + "/" + p

cross = pygame.image.load(fix_path("cross.png"))
circle = pygame.image.load(fix_path("circle.png"))
crossWins = pygame.image.load(fix_path("cross_wins.png"))
circleWins = pygame.image.load(fix_path("circle_wins.png"))

def draw_board():
    pygame.draw.rect(screen,BLACK,(squareWidth - gap,squareHeight - gap, battlefieldSize, battlefieldSize))
    for c in range(rowCount):
        for r in range(rowCount):
            pygame.draw.rect(screen,WHITE,(squareWidth + (r * squareSize) + (r* gap), squareHeight + (c * squareSize) + (c * gap), squareSize, squareSize))
	
    for c in range(rowCount):
        for r in range(rowCount):		
            if comp.field[r][c].tick == playerPiece:
                crossRect = cross.get_rect()
                crossRect.x = squareWidth + (r * squareSize) + (r* gap)
                crossRect.y = squareHeight + (c * squareSize) + (c * gap)
                screen.blit(cross, crossRect)
            elif comp.field[r][c].tick == aiPiece:
                circleRect = circle.get_rect()
                circleRect.x = squareWidth + (r * squareSize) + (r* gap)
                circleRect.y = squareHeight + (c * squareSize) + (c * gap)
                screen.blit(circle, circleRect)
    pygame.display.update()

def is_valid(x, y):
    maximum = rowCount - 1

    if x > maximum or y > maximum or x < 0 or y < 0:
        pass
    else:
        if comp.field[x][y].tick == playerPiece or comp.field[x][y].tick == aiPiece:
            return False
        else:
            return True
    return False

def posxyToXY(posx,posy):
    x = posx - squareWidth - gap
    y = posy - squareHeight - gap

    x = int(x//(squareSize + gap))
    y = int(y//(squareSize + gap))

    return x,y

def winning_move(x, y, piece):
    score = comp.pomoc(x,y,piece)

    if score == 200000:
        return True
    else:
        return False

def printWin(persone):
    if persone == 1:
        crossWinsRect = crossWins.get_rect()
        crossWinsRect.x = int((width-700)/2)
        crossWinsRect.y = int((height-300)/2)
        screen.blit(crossWins, crossWinsRect)
    else:
        circleWinsRect = circleWins.get_rect()
        circleWinsRect.x = int((width-700)/2)
        circleWinsRect.y = int((height-300)/2)
        screen.blit(circleWins, circleWinsRect)

def obtiznost_jp(piece):
    cont = True
    while cont:
        x = random.randint(0,14)
        y = random.randint(0,14)
        
        if comp.field[x][y].tick == emptyPiece:
            cont = False
    comp.newTick.append([x,y])
    comp.field[x][y].updateTick(piece)
    winning_move(x, y, piece)

    return game_over

def difNormal():
    x,y, game_over = comp.main()

    comp.newTick.append([x,y])
    comp.field[x][y].updateTick(aiPiece)
    return game_over

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

turn = 0
#0 - player starts 
#1 - computer starts

comp.createBoard(rowCount)
while game_over == False:
    screen.fill(pygame.Color(255, 255, 255))

    draw_board()

    if turn == ai:
        game_over = difNormal() #-> Hard difficulty
        #game_over = obtiznost_jp(turn + 1) #-> Easy difficulty                     
        #draw_board()
        if game_over == True:
            pass
            printWin(turn + 1)

        turn += 1
        turn = turn % 2

    for event in pygame.event.get():

        if event.type == pygame.QUIT:   
                sys.exit()

        if turn == player:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                xp,yp = posxyToXY(posx,posy)

                
                if is_valid(xp,yp):
                    comp.newTick.append([xp,yp])
                    comp.field[xp][yp].updateTick(turn+1)
                    draw_board()

                    if winning_move(xp, yp, turn + 1):

                        printWin(turn + 1)

                        game_over = True

                    turn += 1
                    turn = turn % 2
                    """
                    player +=1 
                    player = player % 2
                    """
    
    pygame.display.flip()

    clock.tick(60)

button_click = False

while button_click == False:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                sys.exit()

       # if turn == player:
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_click = True