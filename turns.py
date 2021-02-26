"""
Piškvorky
Jiří Průcha, I. ročník
Zimní semestr 2020/2021
Programování I

"""

import comp
"""
PROMĚNNÉ:
(některé proměnné jsou popsané v dalších souborech)

route1, route2 - do těchto listů se ukládá tří políčková "cesta" z určeného bodu. Tedy například do route1 tři políčka vpravo a do route2 tři políčka vlevo

neigh - list pro sousední políčka
zeroes - prázdní políčka
myTicks - políčka obsahující začkrtnutí, které zrovna hledám

"""

nextTurns = []

route1 = []
route2 = []

# Pokud se v programu naskytne chvíle, kdy je možné udělat trojici, pak se zkontroluje, jestli náhodou není lepší tah počkat, aby se v poté rovnou třeba vyhrálo. 
# Tato funkce se zavolá, když se nějaký takovýhle případ vyskytne. Funkce si z listu "twoInARow" čte postupně uložené souřadnice. Na nich následným voláním dalších funkcí hledá, jestli se nedá táhnout lépe.
# Vrací buď true a zásobník s následujícími tahy, nebo false a prázdný list.
def ifThreeIsPossible():
    nextTurns = []
    if len(comp.twoInARow) == 0:
        return False,nextTurns
    else:
        while len(comp.twoInARow) != 0:
            nextTurns = []
            route1 = []
            route2 = []

            position = comp.twoInARow.pop(0)
            x,y = position[0], position[1]
            position = comp.twoInARow.pop(0)
            tick = position[2]

            neigh = neighbors(x,y, tick)
            if neigh != []:
                nextTurns.append([x,y])
                isPossible = tickOnPosition(neigh, tick)
                if isPossible:
                    return True, nextTurns

        return False,[] 

# Zjistí všechny sousedy, na které se dá táhnout. Zároveň poud se nedá táhnout na jedno místo, automaticky se vyřadí i jeho protějšek.
# Například pokud se nedá táhnout do leva, tak se nedá táhnout ani do prava, protože kdybych to nevyřadil, tak hledám trojku, která na jednu stranu nemůže pokračovat. A taková je teď k ničemu.
def neighbors(myX,myY, tick):
    j = 4
    neigh = []
    for _ in range(4):
        j = j - 4 + 1
        isPossible, x, y = comp.switch(myX,myY,j)

        j += 4

        if x != myX and y != myY:
            if isPossible and (comp.field[x][y].tick == 0 or comp.field[x][y].tick == tick):
                neigh.append([x,y,comp.field[x][y].tick,j])
                isPossible, x, y = comp.switch(myX,myY,j)

                if isPossible and (comp.field[x][y].tick == 0 or comp.field[x][y].tick == tick):
                    neigh.append([x,y,comp.field[x][y].tick,j])

                else:
                    neigh.pop(-1)

    return neigh

# Za pomocí dalších funkcí hledá ten nejlepší další tah. Zároveň může dojít k závěru, že žádný takový není. Vrací pouze buď true, nebo false
def tickOnPosition(neigh, tick):
    route1 = []
    route2 = []

    turn = 0
    i = 0
    tunr = -1
    for box in neigh:

        turn += 1
        turn = turn % 2

        if turn == 0:
            x1,y1,tick1,j1 = box[0],box[1],box[2],box[3]
            route1 = route(box)
        else:
            x2,y2,tick2,j2 = box[0],box[1],box[2],box[3]
            route2 = route(box)

        if turn == 1:
            if whatIsOnTheRoute(tick):
                i,k = whereIsTick(tick)
                if i == 1:
                    if k == 1:
                        nextTurns.append([x1,y1])
                        return True
                    else:
                        nextTurns.append([x2,y2])
                        return True
                elif i == 0:
                    if k == 1:
                        isPossible, x, y = comp.switch(x1,y1,j1)
                        nextTurns.append([x,y])
                        return True
                    else:
                        isPossible, x, y = comp.switch(x2,y2,j2)
                        nextTurns.append([x,y])
                        return True
                else:
                    if k == 1:
                        isPossible, x, y = comp.switch(x1,y1,j1+4)
                        nextTurns.append([x,y])
                        return True
                    else:
                        isPossible, x, y = comp.switch(x2,y2,j2+4)
                        nextTurns.append([x,y])
                        return True
    return False


# Vrací místo, kde se nachází námi hledaný tick.
def whereIsTick(tick):
    for i in range(len(route1)):
        if route1[i] == tick:
            return i,1

    for i in range(len(route1)):

        if route2[i] == tick:
            return i,2

def whatIsOnTheRoute(tick):
    zeroes = 0
    myTicks = 0
    for i in range(len(route1)):

        if route1[i] or route2[i] == (tick%2)+1:
            return False

        if route1[i] == 0:
            zeroes += 1
        elif route1[i] == tick:
            myTicks += 1

        if route2[i] == 0:
            zeroes += 1
        elif route2[i] == tick:
            myTicks += 1

    if myTicks == 0:
        return False
    else:
        return True

# Vytváří cestu. Zkontroluje vždy dva sousedy na určenou stranu. Například tedy pravého souseda a ještě jednoho víc vpravo. Z toho vytváří "cestu", kterou vrací.
def route(box):
    x,y,tick,j = box[0],box[1],box[2],box[3]
    route = []
    route.append(tick)
    for _ in range(2):
        isPossible, x, y = comp.switch(x,y,j)
        if isPossible:
            route.append(comp.field[x][y].tick)
        else:
            route.append((tick%2)+1)

    return(route)