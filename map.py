import sys
import random

def readMap(file):
	try:
		src = open(file)	#opens file as read-only
	except:
		print "Input File Error:", file, "could not be found."
		#could use th s to gen random map if prompted by user?
		sys.exit(1)

	dimensions = [0,0] #0: height/rows, 1: width/cols
	tilemap = []
	

	try:
		while True:
			i = 0
			row = []
			line = src.readline()
			
			if not line:			#if no line is read
					break
			
			dimensions[1] += 1
			while line[i] != '\n':
				if line[i].upper() == 'F':
					row.append(0)
				elif line[i].upper() == "W":
					row.append(1)
				else:
					row.append('x')

				i += 1

			if i > dimensions[0]:
				dimensions[0] = i		

			tilemap.append(row)

	except:
		print "Format Error: File does not match expected input. See README for formatting tips."
		sys.exit(2)

	src.close()
	map_info = [dimensions, tilemap]
	return map_info

	
#creates a new map either based off the user input or a random number when prompted by the user
def newMap():
    f = open("newMap.txt","w+")

    w = int(raw_input("Please enter the number of columns (width): "))
    l = int(raw_input("Please enter the number of rows (length): "))

	#creates a map based off inputted length and width
    for x in range(l):
        for i in range(w):
            if x == 0 or i == 0 or x == l - 1 or i == w - 1:
                f.write('w')
            else:
                f.write('f')

        f.write('\n')

    f.close()
    return "newMap.txt"


def randMap():
	f = open("newMap.txt","w+")

	width = random.randint(4,21)
	length = random.randint(4,21)

	#creates a map based off inputted length and width
	for x in range(length):
		for i in range(width):
			if x == 0 or i == 0 or x == length - 1 or i == width - 1:
				f.write('w')
			else:
				f.write('f')

			f.write('\n')
        
	f.close()

	return "newMap.txt"