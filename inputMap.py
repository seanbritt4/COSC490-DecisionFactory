import sys

def readMap(file):
	try:
		src = open(file)	#opens file as read-only
	except:
		print "Input File Error:", file, "could not be found."
		#could use this to gen random map if prompted by user?
		sys.exit(1)

	dimensions = [0,0] #0: height/rows, 1: width/cols
	tilemap = []
	

	try:
		for lines in range(2):
			line = src.readline()
			dimensions[lines] = int(line)
		
		while True:
			row = []
			line = src.readline()
		
			if not line:							#if no line is read
				break

			for i in range(dimensions[0]):			#reads through lines of file
				if i != '\n':						#ignore newlines
					if line[i].upper() == 'F':
						row.append(0)
					elif line[i].upper() == "W":
						row.append(1)
					else:
						row.append('x')

			tilemap.append(row)

	except:
		print "Format Error: File does not match expected input. See README for formatting tips."
		sys.exit(2)

	src.close()
	# return tilemap
	#may not be needed but can also use the following if height/width info needed:
	map_info = [dimensions, tilemap]
	return map_info
