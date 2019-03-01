'''
    ALEC BOULWARE
    MATT ADAMS
    SEAN BRITTINGHAM

    COSC 490
    SPRING 2019
    DECISION FACTORY AND FRAMEWORK

'''

'''
    TODO: none!

'''

import re
import pygame, sys, time
from pygame.locals import *
from DecisionFactory import *
from map import *

#declare tile colors

PURPLE = (189, 23, 173) #portal
BLACK = (0, 0, 0)       #ground/none
GREEN = (0, 255, 0)     #player
GREY = (130, 130, 130)  #wall

#declare tile types

F = 0
W = 1
G = 2
P = 3
N = 'x' #refers to a spot that cannot be spawned in,

    #note that if a player walks over this spot, it will become F

#assign colors

colors = {

        P : GREEN,
        G : PURPLE,
        F : BLACK,
        W : GREY, 
        N : BLACK
    }

#map for Walter to wander in
tilemap = []

#dimensions
TILESIZE = 40
MAPWIDTH = 10       #default- used if no map file is passed at execution
MAPHEIGHT = 10      #default- used if no map file is passed at execution

#define position globally
position = (0, 0)

#globals for command line tags
INIT_OVER = False
FAST = False
RAND_MAP = False
NO_GRAPHICS = False

'''

'''
def initPlayerAndPortal():
    #check if player or portal already exists in textmap
    global INIT_OVER

    player_exists = False
    portal_exists = False
    global position
    for y in range(0, MAPHEIGHT):
        for x in range(0, MAPWIDTH):
            if tilemap[x][y] == 3:
                if INIT_OVER == False:
                    player_exists = True
                    position = [x, y]
                else:
                    tilemap[x][y] = 0

            if tilemap[x][y] == 2:
                if INIT_OVER == False:
                    portal_exists = True

                else:
                    tilemap[x][y] = 0   

    if player_exists == False:
        #initPlayer
        success = False
        while success == False:
            rx = random.randint(0, MAPWIDTH - 1)
            ry = random.randint(0, MAPHEIGHT - 1)

            if tilemap[rx][ry] != W and tilemap[rx][ry] != N:
                tilemap[rx][ry] = P
                position = [rx, ry]
                success = True

    if portal_exists == False:
        #init portal
        success = False
        while success == False:
            rx = random.randint(1, MAPWIDTH - 2)
            ry = random.randint(1, MAPHEIGHT - 2)
            if tilemap[rx][ry] != W and tilemap[rx][ry] != P and tilemap[rx][ry] != N:
                tilemap[rx][ry] = G
                success = True

'''
    print map to std. out

'''
def printTilemap():
    for y in range(0, MAPHEIGHT):
        for x in range(0, MAPWIDTH):
            print tilemap[x][y],
        print

'''

'''
def determineResult(decision):
    d_ver = 0 #d_ver? I hardly know her! LOL my bad i meant to change it back, x/y were confusing me atm. - In a world where x=y, who can blame thee?
    d_hor = 0 
    if decision == 'up':
        d_ver = -1
    elif decision == 'down':
        d_ver = 1
    elif decision == 'left':
        d_hor = -1
    elif decision == 'right':
        d_hor = 1

    global position
    result = tilemap[position[0] + d_hor][position[1] + d_ver]
    print "Starting:", position
    trying = (position[0] + d_hor, position[1] + d_ver)
    print "Trying:", trying

    if result == W:
        return 'wall'
    elif result == F:
        return 'success'
    elif result == N:
        return 'success'
    elif result == G:
        return 'foundPortal'
    else:
        return 'error'

'''
.

'''
def movePlayer(position, decision):
    global tilemap

    old_x = position[0]
    old_y = position[1]
    tilemap[position[0]][position[1]] = F
    
    if decision == 'up':
        tilemap[position[0]][position[1] - 1] = P
        position[1] = position[1]-1
    elif decision == 'down':
        tilemap[position[0]][position[1] + 1] = P
        position[1] = position[1]+1
    elif decision == 'left':
        tilemap[position[0] - 1][position[1]] = P
        position[0] = position[0]-1
    elif decision == 'right':
        tilemap[position[0] + 1][position[1]] = P
        position[0] = position[0]+1

'''
Fixes Matrix so that y!=x. Ask no questions, just take it for granted,
I don't even understand.
'''
def fixMatrix(matrix):
    newMatrix = [[0 for y in range(MAPHEIGHT)] for x in range(MAPWIDTH)]
    for y in range(MAPHEIGHT):
        for x in range(MAPWIDTH):
            newMatrix[x][y] = matrix[y][x]

    global tilemap
    tilemap = newMatrix 

def main():
    map_file = "map00.txt"

    if len(sys.argv) >= 2:
        for arg in sys.argv:
            if arg == '-noGraphics' or arg == '-ng':
                global NO_GRAPHICS
                NO_GRAPHICS = True
            elif arg == '-initOverride' or arg == '-r':
                global INIT_OVER
                INIT_OVER = True
            elif arg == '-fast' or arg == '-f':
                global FAST
                FAST = True
            elif arg == '-randomMap' or arg == '-rm':
                map_file = newMap(True)
            elif arg == '-newMap' or arg == '-nm':
                map_file = newMap(False)
            else:
                # uses regular expressions to find map file in the format:
                #   map(*)*.txt where they may be any number of characters inbetween
                #   'map' and '.txt'
                m = re.search("map.*\.txt", arg)    #returns Match object or None
                if m:                               #checks for Match object- Match was found
                    map_file = m.string             #returns string of Match object

    global MAPHEIGHT
    global MAPWIDTH
    global tilemap

    map_info = readMap(map_file)
    MAPHEIGHT = map_info[0][1]
    MAPWIDTH = map_info[0][0]
    tilemap = map_info[1]

    #swap tiles to match the input map

    fixMatrix(tilemap)

    #turn off map printing w/ -noGraphics

    if NO_GRAPHICS == False:
        #initialize the display
        pygame.init()
        pygame.display.set_caption("Walter Wanderley")
        DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

    initPlayerAndPortal()
    steps = 0               #steps to find goal
    df = DecisionFactory()  #initialize DecisionFactory

    fast = False

    if len(sys.argv) >= 2:
        for i in range(len(sys.argv)):
            if sys.argv[i] == "-fast" or sys.argv[i] == "-f":
                fast = True

    printTilemap()



    while True:
        if NO_GRAPHICS == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        
        if fast == False:       
            time.sleep(0.08)

        print


        decision = df.get_decision()

        print "Decision: ", decision

        #get result of 'walk'
        result = determineResult(decision) 
        df.put_decision(decision)

        print "Result: ", result

        if result == 'foundPortal':
            print "Found portal in", steps, "steps!\n"
            df.put_result('success')
           #df.put_decision(decision)
            pygame.quit()
            sys.exit()

        else:
            df.put_result(result)
            #df.put_decision(decision)
            steps += 1
            print "Steps: ", steps

        if result == 'success':
            movePlayer(position, decision)
            df.put_result('success')
            #df.put_decision(decision)

            printTilemap()

        if NO_GRAPHICS == False:
            #draw map to screen 
            for column in range(MAPWIDTH):
                for row in range(MAPHEIGHT):
                    pygame.draw.rect(DISPLAYSURF, colors[tilemap[column][row]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

            pygame.display.update()

        raw_input("Press Enter to Quit")
        sys.exit()


'''
    Flow control

'''
if __name__ == "__main__":
    main()