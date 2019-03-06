import random
from Stack import SuperStack

#import numpy as np

class DecisionFactory:
	def __init__(self, name='Walter Wanderley'):
		self.name = name
		self.directions = ['wait', 'up', 'down', 'right', 'left']
		self.failed_directions = []
		self.last_result = 'start'
		self.last_direction = 'wait'

		self.counter = 0
		self.next_direction = 'wait'
		self.popping = False
		self.poss_moves = [1, 2, 3, 4]
		self.stack = SuperStack()
	#Note: we have relativistic coordinates recorded here, since the map
	# is relative to the player's first known and recorded position:
	#self.state.pos = (0,0)

	def get_decision(self, verbose = True):
		#return self.random_direction()
		# return self.better_than_random()
		#return self.snake()
		return self.DFS_Search()

	#week 1
	def random_direction(self):
		#random.randint(0,4) #Includes wait state
		r = random.randint(1,4) #Does NOT include wait state
		self.stack.superPush(r)
		loc = [self.stack.current_location[0], self.stack.current_location[1]]
		self.stack.discovered.append(loc)
		return self.directions[r]
	
	#takes a direction [1..4] and returns true if that direction is not in memory
	def checkNonRemembered(self, direction):
		if direction == 1:
			loc = [self.stack.current_location[0], self.stack.current_location[1]+1]
			for i in range(len(self.stack.discovered)):
				if loc == self.stack.discovered[i]:
					return False 
			for i in range(len(self.stack.discoveredWalls)):
				if loc == self.stack.discoveredWalls[i]:
					return False
		if direction == 3:
			loc = [self.stack.current_location[0]+1, self.stack.current_location[1]]
			for i in range(len(self.stack.discovered)):
				if loc == self.stack.discovered[i]:
					return False
			for i in range(len(self.stack.discoveredWalls)):
				if loc == self.stack.discoveredWalls[i]:
					return False 
		if direction == 2:
			loc = [self.stack.current_location[0], self.stack.current_location[1]-1]
			for i in range(len(self.stack.discovered)):
				if loc == self.stack.discovered[i]:
					return False
			for i in range(len(self.stack.discoveredWalls)):
				if loc == self.stack.discoveredWalls[i]:
					return False 
		if direction == 4:
			loc = [self.stack.current_location[0]-1, self.stack.current_location[1]]
			for i in range(len(self.stack.discovered)):
				if loc == self.stack.discovered[i]:
					return False
			for i in range(len(self.stack.discoveredWalls)):
				if loc == self.stack.discoveredWalls[i]:
					return False
		return True
	#auxiliary function for DFS_Search, replaces a possible move with 'x'
	def delPossMove(self, dir):
		self.poss_moves[dir-1] = 'x';
	
	#pops the stack and returns the reverse direction
	def moveBack(self):
		return self.stack.superPop()

	#performs DFS search on the tilemap, painstakingly	
	def DFS_Search(self):
		loc = self.stack.current_location
		
		self.popping = False
		if self.last_result == 'success' or self.last_result == 'start':
			self.stack.discovered.append([loc[0],loc[1]])
			self.poss_moves = [1,2,3,4]
		#reset location when player runs into wall
		if self.last_result == 'wall':
			self.stack.discoveredWalls.append([loc[0],loc[1]])
			if self.stack.moves[-1] == 1:
				self.stack.current_location = [loc[0], loc[1]-1]
			elif self.stack.moves[-1] == 2:
				self.stack.current_location = [loc[0], loc[1]+1]
			elif self.stack.moves[-1] == 3:
				self.stack.current_location = [loc[0]-1, loc[1]]
			elif self.stack.moves[-1] == 4:
				self.stack.current_location = [loc[0]+1, loc[1]]
			del self.stack.moves[-1]
		'''	
		#delete last move that was made
		for i in range(len(self.poss_moves)):
			if self.last_result != 'start':
				r = self.stack.moves[-1]
				if r == 1:
					r = 2
				elif r == 2:
					r = 1
				elif r == 3:
					r = 4
				elif r == 4:
					r = 3
				self.delPossMove(r)
		'''
		#delete poss_moves resulting in discovered walls in each direction
		if not self.checkNonRemembered(1):
			self.delPossMove(1)
		if not self.checkNonRemembered(2):
			self.delPossMove(2)
		if not self.checkNonRemembered(3):
			self.delPossMove(3)
		if not self.checkNonRemembered(4):
			self.delPossMove(4)
		isempty = True
		for i in range(len(self.poss_moves)):
			if self.poss_moves[i] != 'x':
				isempty = False
				'''
				if self.poss_moves[1] != 'x' and self.poss_moves[2] != 'x':
					self.poss_moves = [1,2,3,4]	
					self.stack.superPush(self.poss_moves[2])
					return self.directions[self.poss_moves[2]]
				'''
				self.stack.superPush(self.poss_moves[i])
				self.poss_moves = [1,2,3,4]
				
				return self.directions[self.poss_moves[i]]
		if isempty:
			r = self.stack.superPop()
			self.popping = True
			self.poss_moves = [1,2,3,4]
			return self.directions[r]
		if self.last_result == 'start' or self.last_result == 0:
			self.stack.superPush(self.directions[1])
			return self.directions[1]
		

	#week 2
	def better_than_random(self):
		r = self.random_direction()

		self.failed_directions.extend(self.last_direction)

		if self.last_result != 'success':
			self.failed_directions.extend(self.last_direction)
			r = random.randint(1,4)

			while self.directions[r] in self.failed_directions:
				r = random.randint(1,4)

			return self.directions[r]

		else:	
			self.failed_directions = []

			r = self.random_direction()
			return r

#week 3
#makes the player character snake its way through the entire grid 
	def snake(self):
		self.counter += 1
		# print "we are snaking "
		print self.last_direction
		r= 4

		#makes the player character go up once it has gone all the way left once it has gone all the way up one time it uses a second if to make it go down
		#it then sets next direction to right so the player will move right once it moves down
		if self.last_result != 'success' and self.last_direction == 'left':
			r= 1
			if self.last_direction == 'left' and self.counter >15:
				r = 2
				self.next_direction = 'right'
			
			return self.directions[r]

		#this makes sure the player continues moving up until it hits the top barrier
		if self.last_result == 'success' and self.last_direction =='up':		
			r = 1
			return self.directions[r]
			
		#this makes it so once it hits the top barrier it will move right
		if self.last_result != 'success' and self.last_direction == 'up':
			r = 3
			return self.directions[r]

		#this makes sure it continues moving right until it hits a wall
		if self.last_result == 'success' and self.last_direction == 'right':
			r = 3
			return self.directions[r]

		#this if makes the user play move down once it hits a wall going right and sets the next direction to left so the player 
		#moves correctly
		if self.last_result != 'success' and self.last_direction == 'right':
			r = 2
			self.next_direction = 'left'
			return self.directions[r]

		#this moves the player either left or right once it has gone below the top layer
		if self.last_result == 'success' and self.last_direction == 'down':
			r = 4
			if self.next_direction == 'right':
				r = 3

			return self.directions[r]

		# print "going left"
		return self.directions[r]

	def put_result(self, result):
		self.result = result
		self.last_result = result

	def put_decision(self, decision):
		self.last_direction = decision

