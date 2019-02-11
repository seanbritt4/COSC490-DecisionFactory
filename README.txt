TODO: -implement a way to add portal and player location on the textfile without having them affected by the 
initPortalAndPlayer() function, and maybe also an 'override' command line parameter that uses initPortalAndPlayer() anyway, just 
for added flexability 
      -make printing the graphical map to the screen optional, perhaps through a command line parameter

CHANGES: 
      2/11/19 Sean
      -Matt, I undid almost everything you added... Not on purpose,my bad. I just didnt read the README before startng.
              lesson learned, I will read it first next time. I messed with the steps and print out but Ill change it back. 
              Not trying to be stubborn about it, just an idiot that didn't read.
      -However, I did more than just undo Matss, code. Made a first attempt at "better than random". Suffering when goal is 
            not on a wall, but consistently finding it when it is. Essientially the player runs around the wall... There is 
            a lot of room for improvement but not enough time this morning.
            
            
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
changed the following (I know there is a bit of lost of meaning with these variable names but it is the most efficient method that I could come up with):
GRND 	->	F	#floor
WALL 	->	W 	#wall
PLAYER	->	P 	#player
PORTAL	->	G 	#goal
NONE 	-> 	N 	#none
