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
def newMap(random_map):
	des = open("newMap.txt","w+")

	if random_map:
		rows = random.randint(4,21)
		cols = random.randint(4,21)
	else:	
		cols = int(raw_input("Please enter the number of columns (width): "))
		rows = int(raw_input("Please enter the number of rows (length): "))

 	for row in range(rows):
		for col in range(cols):
			if row == 0 or row == (rows -1)or col == 0 or col == (cols -1):
				des.write('W')
				if col == (cols - 1):
					des.write('\n')
			else:
				des.write("F")


	des.close()
	return "newMap.txt"