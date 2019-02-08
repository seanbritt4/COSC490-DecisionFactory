'''
    ALEC BOULWARE
    MATT ADAMS
    SEAN BRITTINGHAM

    COSC 490
    SPRING 2019
    DECISION FACTORY AND FRAMEWORK
'''
'''
    GOALS: 
        -Still need to make "better than random"?

    KNOWN ISSUES:
        -rows in the tilemap appear as columns in the real-time matrix & 
            the game-screen.
            
    
    CHANGE LOG:
        Fri.  Feb 8:
        	-work on map input. work is too busy to do anything too serious...
        		see README for formatting
        		NOTE:
				I changed the following (I know there is a bit of lost of meaning
				with these variable names but it is the most efficient method
				that I could come up with):
			GRND 	->	F	#floor
			WALL 	->	W 	#wall
			PLAYER	->	P 	#player
			PORTAL	->	G 	#goal
			NONE 	-> 	N 	#none


        Thurs Feb 7:
            -formatting
            -added some comments
            -GROUND to GRND, keeps tile map squre and easier to read
            -redesigned map to wall is on border, player was spawning out of bounds
            -edited movePlayer so that the axes correspond properly to position 
            -fixed indentation in main()
            -made position variable global

    TODO:
        -add textfile input for map
        -eventually add a scrolling map for larger sized maps
        -player finding portal but not moving in gui... minor issue but might 
            be nice to look into. thinking it could be as simple as "refreshing"
            before registering that the portal was found. -SB

    TIP:
        run with the following: python framework.py > output.py to send output to 
            text file. This just makes reviewing results a little easier than scrolling
            through the terminal (personal preference i guess) -SB
'''

import pygame, sys, time
from pygame.locals import *
from DecisionFactory import *
from inputMap import readMap
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

#hard-coded test map, note the NONE's in the middle and how they appear 
#                     in the real-time array when running
tilemap = [
            [W, W, W, W, W, W, W, W, W, W],
            [W, F, F, F, F, F, F, F, F, W],
            [W, F, F, F, F, F, F, F, F, W],
            [W, F, F, F, F, F, F, F, F, W],
            [W, F, F, F, N, N, F, F, F, W],
            [W, F, F, F, F, F, F, F, F, W],
            [W, F, F, F, F, F, F, F, F, W],
            [W, F, F, F, F, F, F, F, F, W],
            [W, F, F, F, F, F, F, F, F, W],
            [W, W, W, W, W, W, W, W, W, W],
          ]

#dimensions
TILESIZE = 40
MAPWIDTH = 10
MAPHEIGHT = 10

#define position globally
position = (0, 0)
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
        rx = random.randint(0, MAPWIDTH - 1)
        ry = random.randint(0, MAPHEIGHT - 1)

        if tilemap[rx][ry] != W and tilemap[rx][ry] != N:
            tilemap[rx][ry] = P
            print "player rx:", rx
            print 'player ry:', ry
            position = [rx, ry]
            success = True

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
    d_ver = 0 #d_ver? I hardly know her! LOL my bad i meant to change it back, x/y were confusing me atm
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
                    
        time.sleep(0.07)
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
            
            movePlayer(position, decision)

    
        for row in range(MAPWIDTH):
    		for column in range(MAPHEIGHT):
    			pygame.draw.rect(DISPLAYSURF, colors[tilemap[column][row]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
        
        # steps += 1
    	pygame.display.update()
        # print "Steps: ", steps


'''
    Flow control
'''
if __name__ == "__main__":

	if len(sys.argv) >= 2: #reads file name, ignores all other arguments passed
		map_info = readMap(sys.argv[1])
		MAPHEIGHT = map_info[0][0]
		MAPWIDTH = map_info[0][1]
		tilemap = map_info[1]
	
		print "map_info:\n", map_info
		print "MAPHEIGHT:\n", MAPHEIGHT
		print "MAPWIDTH:\n", MAPWIDTH
		print "tilemap:\n", tilemap
	
	main()