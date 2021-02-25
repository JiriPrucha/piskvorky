import comp

def ifThreeIsPossible():
    if len(comp.twoInARow) == 0:
        return False,0,0
    else:
        for position in comp.twoInARow:
            if len(position) == 2:
                x,y =  position[0],position[1]
                tick = 10000
            else:
                tick = position[2]
            if tick != 10000:
                neigh = neighbors(x,y,tick)
                ifTrue = tickOnPosition(neigh, tick)
                if ifTrue:
                    return True, x,y

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
    
def tickOnPosition(neigh, myTick):
    route = []
    i = 0
    #score = 0
    if neigh == []:
        return False
    else:
        for box in neigh:
            x,y,tick,j = box[0],box[1],box[2],box[3]
            cont = True
            while cont:
                i += 1
                route.append([x,y,tick,j])
                isPossible, x, y = comp.switch(x,y,j)
                if isPossible:
                    if comp.field[x][y].tick == myTick:
                        cont = False
                    elif comp.field[x][y].tick == 0:
                        if i == 2:
                            cont = False
            myBox = route.pop(-1)
            x,y,tick,j = myBox[0],myBox[1],myBox[2],myBox[3]
            if myTick == 1:
                #score = comp.field[x][y].rankX()
                #if score > 30000:
                comp.field[x][y].updateX(10000)
                return True
            elif myTick == 2:
                #score = comp.field[x][y].rankO()
                #if score > 30000:
                comp.field[x][y].updateO(10000)
                return True
        return False