import random

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
	#Note: we have relativistic coordinates recorded here, since the map
	# is relative to the player's first known and recorded position:
	#self.state.pos = (0,0)

	def get_decision(self, verbose = True):
		# return self.random_direction()
		# return self.better_than_random()
		return self.snake()

	#week 1
	def random_direction(self):
		#random.randint(0,4) #Includes wait state
		r = random.randint(1,4) #Does NOT include wait state
		return self.directions[r]

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

