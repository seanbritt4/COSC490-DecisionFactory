'''
	should work with rest of framework but have not tested it yet
	
	each stack class oobject created is actually two stacks
		one tracks all moves made (never popped from)
		other is to be used if Walter needs to return

	handles return direction in superPop

	coordinates are included but tbh i didnt really understand what their intended use was
	

	also have you guys seen the spice girls lately. i kinda hoped one of them were looking rough but they all held up pretty well. good for them.
'''
class SuperStack():
	def __init__(self):
		self.moves = [0]					#list of moves made by player
		self.discovered = []			#list of discovered tiles
		self.discoveredWalls = []	#list of discovered walls
		self.current_location = [0,0]	#(x,y) Walters coordinates
		self.size = 0					#number of elements in list

	
	def superPop(self):
		move = self.moves.pop()

		'''
			return opposite direction, Walter can use this to go back home
		'''
		if move == 'up':
			move = 'down'
		elif move == 'down':
			move = 'up'
		elif move == 'left':
			move = 'right'
		elif move == 'right':
			move = 'left'
		if move == 1:
			move = 2
		elif move == 2:
			move = 1
		elif move == 3:
			move = 4
		elif move == 4:
			move = 3

		# appropriately update Walters position in the world
		self.toCoord(move)
		return move


	'''
		updates stack size, stack (adds latest move to end of stack), Walters coordinates,
		and discovered tiles stack
	'''
	def superPush(self, move):
		self.size += 1
		self.moves.append(move)
		self.toCoord(move)
	#	self.discovered.append(move)

	#updates coordinates
	def toCoord(self, move):
		if move == 'up' or move == 1:
			self.current_location[1] += 1
		if move == 'down' or move == 2:
			self.current_location[1] -= 1
		elif move == 'left' or move == 4:
			self.current_location[0] -= 1
		elif move == 'right' or move == 3:
			self.current_location[0] += 1

		return self.current_location


	'''
		following functions can be used for debugging. Dont see any other reason to use them
	'''

	def getSize(self):
		return self.size
	def printMoves(self):
		print self.moves
	def printDiscovered(self):
		print self.discovered
	def printAll(self):
		print "Moves:"
		print self.moves
		print "Discovered"
		print self.discovered
