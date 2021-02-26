"""
Piškvorky
Jiří Průcha, I. ročník
Zimní semestr 2020/2021
Programování I

"""

import sys
import os
import random
import pygame
from pygame import Rect, Vector2, Color

import comp

"""
PROMĚNNÉ:
(některé proměnné jsou popsané v dalších souborech)

width, height - šířka a výška obrazovky, na které se zobrazuje program. Neodporučuji dávat příliš vysoké hodnoty, nemusí se to poté vejít na monitor. Malá hodnota zase nemusí být dostatečná pro zobrazení všeho.

rowCount - počet řádků/sloupců. Čím vyšší hodnota, tím větší bude místo pro hru.
player, ai - určuje, při jakém tahu hraje jaký hráč. Pokud chcete mít možnost hrát s dalším hráčem, je nutné "ai" změnit na číslo 2 a vyšší.

emptyPiece, playerPiece, aiPiece - Určuje, kdo má jaký znak

squareSize - Velikost jednoho políčka. Nedoporučuji měnit. Obrázky křížků a kroužků jsou vytvořené pro tuto velikost.
gap - Mezera mezi políčky

battlefieldSize - Potřebná velikost pro čtverečkované pole

game_over - True: pokud byl tah výherní. False: Pokud nebyl výherní

squareWidth, squareHeight - Určuje vzdálenost herného pole od kraje obrazovky. 

posx, posy - Relativní pozice myši vůči obrazovce, na které je hra zobrazována. Z těhto souřadnic se musí ještě zjistit, kam vlastně člověk na poli kliknul. Nebo jestli náhodou neklikl mimo.

x, y - Souřadnice nějakého políčka
"""

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
ai = 1

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

# Proměnné pro obrázly. cross - křížek, circle - kolečko, crossWins - výherní obrázek křížku, circleWins - výherní obrázek kolečka

cross = pygame.image.load(fix_path("cross.png"))
circle = pygame.image.load(fix_path("circle.png"))
crossWins = pygame.image.load(fix_path("cross_wins.png"))
circleWins = pygame.image.load(fix_path("circle_wins.png"))
drawPicture = pygame.image.load(fix_path("draw.png"))

# Vykreslí herní pole. Pokud je v poli křížek nebo kolečko, vykreslí i to.
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

# Kontroluje, zdali jde na toto místo vložit požadovaná kamen. Udělá to tím způsobem, že zkontroluje, zdali tyto souřadnice nejsou přiliš vysoké nebo malé a jestli na pozici s těmito souřadnicemi není už nějaký kámen. Vrací True/False
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

# Mění relativní pozici myši na x a y pozici v herním poli
def posxyToXY(posx,posy):
    x = posx - squareWidth - gap
    y = posy - squareHeight - gap

    x = int(x//(squareSize + gap))
    y = int(y//(squareSize + gap))

    return x,y

# Zjistí, zda hráč položil výherní káman, za pomocí funkce "toWhichSide()", kterou využíváme i při hře počítačem. Ta vrací nějaké hodnocení pozice. Pokud to se rovná hodnocení pro 5 kamenů v řadě, pak vrací true, jinak false.
def winning_move(x, y, piece):
    score = comp.toWhichSide(x,y,piece)

    if score == 200000:
        return True
    else:
        return False

# Po zavolání na obrazovce zobrazí výherní obrázek
def printWin(persone):
    if persone == 1:
        crossWinsRect = crossWins.get_rect()
        crossWinsRect.x = int((width-700)/2)
        crossWinsRect.y = int((height-300)/2)
        screen.blit(crossWins, crossWinsRect)
    elif persone == 10:
        drawRect = drawPicture.get_rect()
        drawRect.x = int((width-700)/2)
        drawRect.y = int((height-300)/2)
        screen.blit(drawPicture, drawRect)
    else:
        circleWinsRect = circleWins.get_rect()
        circleWinsRect.x = int((width-700)/2)
        circleWinsRect.y = int((height-300)/2)
        screen.blit(circleWins, circleWinsRect)

# Lehká obtížnost. Neboli Obtížnost Jiří Průcha. Funguje na náhodném vybírání volných pozic za pomocí funkce "random"
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

# "Těžká" obtížnost. Funkce, která se stará o zavolání do souboru "comp.py" a o zapisování tahů do třídy Board
def difNormal():
    x,y, game_over = comp.main()

    if x == 150:
        draw = 1
    else:
        comp.newTick.append([x,y])
        comp.field[x][y].updateTick(aiPiece)
    return game_over

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Proměnná, která určuje, jaký hráč je na tahu. Pokud se nezměnili proměnné player a ai, tak: turn = 0 - začíná hráč, turn = 1 - začíná počítač
turn = 0
#0 - player starts 
#1 - computer starts

#Pomocník při hlídání, jestli nastala remíza nebo ne
draw = 0

"""
Hlavní část celého programu. Opakuje se, dokud se nebude proměnná game_over rovnat True.
Pokud je na tahu počítač, tak se zavolá funkce difNormal(). 
Jinak se čeká na validní kliknutí myší od hráče.
V poslední možnosti se program vypne, pokud se uživatel rozhodne ho vypnout například křížkem.
"""
comp.createBoard(rowCount)
while game_over == False:
    screen.fill(pygame.Color(255, 255, 255))

    draw_board()

    if turn == ai:
        game_over = difNormal() #-> Hard difficulty - Stačí zakomentovat tento řádek a odkomentovat další řádek. Tím se obtížnost zlehčí
        #game_over = obtiznost_jp(turn + 1) #-> Easy difficulty                     
        if game_over == True:
            if draw == 0:
                printWin(turn + 1)
            else:
                printWin(10)
        turn += 1
        turn = turn % 2

    for event in pygame.event.get():

        if event.type == pygame.QUIT:   
                sys.exit()

        if turn == player:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                x,y = posxyToXY(posx,posy)

                
                if is_valid(x,y):
                    comp.newTick.append([x,y])
                    comp.field[x][y].updateTick(turn+1)
                    draw_board()

                    if winning_move(x, y, turn + 1):

                        printWin(turn + 1)

                        game_over = True

                    turn += 1
                    turn = turn % 2

                    # Druhá nutnost pro hraní dvou hráčů proti sobě je toto odkomentovat. Akorát to říká, že každý tah hraje hráč. A je jedno, jestli tah se rovná 0 nebo 1. Po tomto a změně ai na 2 a vícmůžou hrát dva proti sobě
                    """
                    player +=1 
                    player = player % 2
                    """
    
    pygame.display.flip()

    clock.tick(60)

button_click = False