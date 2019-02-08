ALEC BOULWARE
MATT ADAMS
SEAN BRITTINGHAM

COSC 490
SPRING 2019
DECISION FACTORY AND FRAMEWORK
 
GOALS: 
    -Still need to make "better than random"?

KNOWN ISSUES:
    -rows in the tilemap appear as columns in the real-time matrix & 
        the game-screen.


CHANGE LOG:
    Fri.  Feb 8:
      -work on map input. work is too busy to do anything too serious...
        see lower for formatting and other related change

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
        before registering that the portal was found.
    -move default map from factory.py to map00.txt or default_map.py (hard-code
        this to be read, overwrite if map file is passed)
    -map reading is only supported if map size is LESS THAN 10 (0-9)
        (this is an easy fix and will add asap)
    -limit map sizes? 
        lower bound: 4 (anything lower is pointless)
        upper bound: ???

TIP (take it or leave it):
    run with the following: python framework.py > output.py to send output to 
        text file. This just makes reviewing results a little easier than scrolling
        through the terminal (personal preference i guess)

READING MAPS BY INPUT
HOW TO DO:
python framework.py <map_file_name>
(test map will be used if no map file is passed)

FORMAT:
<height>
<width>
<matrix (NOT case-sensitive)>

ex:
5
5
WWWWW
WFFFW
WFFFW
WFFFW
WWWWW

NOTE:
Tried to implement with changing as little code in framework.py as possible though i did change the following 
(I know there is a bit of lost of meaning with these variable names but it is the most efficient method that I could come up 
with(later edit: might be uneccessary and can change back if needed):
GRND 	->	F	#floor
WALL 	->	W 	#wall
PLAYER	->	P 	#player
PORTAL	->	G 	#goal
NONE 	-> 	N 	#none
