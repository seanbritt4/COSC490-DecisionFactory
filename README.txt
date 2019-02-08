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
