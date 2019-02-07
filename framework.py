'''
    ALEC BOULWARE
    MATT ADAMS
    SEAN BRITTINGHAM

    COSC 490
    SPRING 2019
    DECISION FACTORY AND FRAMEWORK
'''

'''
    KNOWN ISSUES:
        "-directions not corresponding...
                    UP moves player left,
                    RIGHT moves player down,
                    etc

            this leads to errors when choosing a direction to move & allows
                player to walk through walls

    CHANGES:
        -formatting
        -added some comments
        -GROUND to GRND, keeps tile map squre and easier to read
        -redesigned map to wall is on boarder, player was spawning out of bounds

    FIXED:
        -player duplicating; movement improved

    -SB
'''

import pygame, sys, time
from pygame.locals import *
from DecisionFactory import *

#declare tile colors
PURPLE = (189, 23, 173) #portal
BLACK = (0, 0, 0)       #ground
GREEN = (0, 255, 0)     #player
GREY = (130, 130, 130)  #wall

#declare tile types
GRND = 0
WALL = 1
PORTAL = 2
PLAYER = 3

#assign colors
colors = {
		PLAYER : GREEN,
		PORTAL : PURPLE,
        GRND : BLACK,
        WALL : GREY
	}

#hard-coded test map
tilemap = [
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, GRND, GRND, GRND, GRND, GRND, GRND, GRND, GRND, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
          ]

#dimensions
TILESIZE = 40
MAPWIDTH = 10
MAPHEIGHT = 10

#pygame set-up
pygame.init()
pygame.display.set_caption("Decision Factory")  #names window
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

'''

'''
def initPlayerAndPortal():
    #initPlayer
    success = False
    global position
    while success == False:
        rx = random.randint(1, MAPWIDTH - 1)
        ry = random.randint(1, MAPHEIGHT - 1)
        if tilemap[rx][ry] != WALL:
            tilemap[rx][ry] = PLAYER
            print "player rx:", rx
            print 'player ry:', ry
            position = [rx, ry]
            success = True

    success = False
    while success == False:
        rx = random.randint(1, MAPWIDTH - 2)
        ry = random.randint(1, MAPHEIGHT - 2)
        if tilemap[rx][ry] != WALL and tilemap[rx][ry] != PLAYER:
            tilemap[rx][ry] = PORTAL
            success = True

'''
    print map to std. out
'''
def printTilemap():
    for x in range(0, MAPHEIGHT):
        for y in range(0, MAPWIDTH):
            print tilemap[x][y],
        print

'''

'''
def determineResult(decision):
    d_ver = 0
    d_hor = 0
    if decision == 'up':
        d_ver = -1
    elif decision == 'down':
        d_ver = 1
    elif decision == 'left':
        d_hor = -1
    elif decision == 'right':
        d_hor = 1

    result = tilemap[position[0] + d_hor][position[1] + d_ver]

    print "Starting:", position
    trying = (position[0] + d_hor, position[1] + d_ver)
    print "Trying:", trying
  
    if result == WALL:
        return 'wall'
    elif result == GRND:
        return 'success'
    elif result == PORTAL:
        return 'foundPortal'
    else:
        return 'error'

'''

'''
def movePlayer(position, decision):
    global tilemap

    old_x = position[0]
    old_y = position[1]

    tilemap[position[0]][position[1]] = GRND
    
    if decision == 'up':
        tilemap[position[0] - 1][position[1]] = PLAYER
        position[0] = position[0]-1
    elif decision == 'down':
        tilemap[position[0] + 1][position[1]] = PLAYER
        position[0] = position[0]+1
    elif decision == 'left':
        tilemap[position[0]][position[1] - 1] = PLAYER
        position[1] = position[1]-1
    elif decision == 'right':
        tilemap[position[0]][position[1] + 1] = PLAYER
        position[1] = position[1]+1

    print "Position:", position


def main():
    initPlayerAndPortal()
    steps = 0               #steps to find goal
    df = DecisionFactory()  #initialize DecisionFactory
    # position = (0, 0)       #set player position

    while True:
    	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                    
            time.sleep(0.7)
            print
            printTilemap()

            decision = df.get_decision()
            print "Decision: ", decision
            #get result of 'walk'
            result = determineResult(decision) 
            print "Result: ", result
           

            if result == 'foundPortal':
                print "Found portal in", steps, "steps!\n"
                df.put_result('success')
                pygame.quit()
                sys.exit()
            else:
                df.put_result(result)
            # print "Decision:", decision
            
            if result == 'success':
                steps += 1
                print "Steps: ", steps
                
                print "pos 1:", position
                movePlayer(position, decision)
                print "pos 2:", position

    	
        for row in range(MAPHEIGHT):
    		for column in range(MAPWIDTH):
    			pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
        
        # steps += 1
    	pygame.display.update()
        # print "Steps: ", steps


'''
    Flow control
'''
if __name__ == "__main__":
    main()
