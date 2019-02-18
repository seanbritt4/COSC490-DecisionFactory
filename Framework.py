
 
'''

    ALEC BOULWARE

    MATT ADAMS

    SEAN BRITTINGHAM



    COSC 490

    SPRING 2019

    DECISION FACTORY AND FRAMEWORK

'''



'''

TODO: -add a way to initialize the portal/player where we want in the text file, 

        and not have it affected by the initPlayerAndPortal() function



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

#map for Walter to wander in

tilemap = []



#dimensions

TILESIZE = 40

MAPWIDTH = 10       #default- used if no map file is passed at execution

MAPHEIGHT = 10      #default- used if no map file is passed at execution



#define position globally

position = (0, 0)



#pygame set-up

pygame.init()

pygame.display.set_caption("Walter Wanderley")  #names window

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





#creates a new map either based off the user input or a random number when prompted by the user
def newMap():

    f = open("newMap.txt","w+")


    #holds width input
    r = raw_input("Please enter a new width or random for a random number: ")

    
    #determines if a random number or user inputed is put into the file
    if r == 'random':

        width = str(random.randint(4,21))

        wide = int(width)
        f.write(width + '\n')

    else:
        width = r
        wide = int(width)
        f.write(width+ '\n')
        #holds length input 
    l = raw_input("Please enter a new length or random for a random number: ")

   

    #if the user asks for random this will make a random length
    if l == 'random':

        length = str(random.randint(4,21))

        lent = int(length)
        f.write(length + '\n')

    else:
        length = l
        lent = int(length)
        f.write(length + '\n')


#creates a map based off inputted length and width
    for x in range(lent):
        for i in range(wide):

            if x == 0 or i == 0 or x == lent - 1 or i == wide - 1:

                f.write('w')

            else:
                f.write('f')

        f.write('\n')


    f.close()



def main():

    response = raw_input("Would you like to make your own map? Y/N: ")

    if response == 'y' or response == "Y":
        
        newMap()
        map_file = "newMap.txt"

    else:

        if len(sys.argv) >= 2: #reads file name, ignores all other arguments passed

            map_file = sys.argv[1]

        else:

            map_file = "map00.txt"



    global MAPHEIGHT

    global MAPWIDTH

    global tilemap



    map_info = readMap(map_file)

    MAPHEIGHT = map_info[0][1]

    MAPWIDTH = map_info[0][0]

    tilemap = map_info[1]

    #swap tiles to match the input map

    fixMatrix(tilemap)

    #re-initialize the display to match map size

    DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))



    initPlayerAndPortal()

    steps = 0               #steps to find goal

    df = DecisionFactory()  #initialize DecisionFactory



    printTilemap()

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:

                pygame.quit()

                sys.exit()

                    

        time.sleep(0.8)

        print



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

        steps += 1

        print "Steps: ", steps

        if result == 'success':

            movePlayer(position, decision)



            printTilemap()



                #draw map to screen 

        for column in range(MAPWIDTH):

            for row in range(MAPHEIGHT):

                pygame.draw.rect(DISPLAYSURF, colors[tilemap[column][row]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

        

        pygame.display.update()





'''

    Flow control

'''

if __name__ == "__main__":

    main()