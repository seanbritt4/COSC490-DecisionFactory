import sys
from random import randint

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