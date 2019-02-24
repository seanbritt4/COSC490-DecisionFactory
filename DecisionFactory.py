import random

#import numpy as np



class DecisionFactory:

	def __init__(self, name='Walter Wanderley'):

		self.name = name

		self.directions = ['wait', 'up', 'down', 'right', 'left']

		self.failed_directions = []

		self.last_result = 'start'

		self.last_direction = 'wait'



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
	def snake(self):


		print "we are snaking "

		r= 4


		if self.last_result != 'success':

			r= 1
			"first step up"
			return self.directions[r]

		if self.last_result == 'success' and self.last_direction =='up':		

			r = 1
			print "going up"
			return self.directions[r]

		if self.last_result != 'success' and self.last_direction == 'up':

			r = 3
			print "first step right"
			return self.directions[r]


		if self.last_result == 'success' and self.last_direction == 'right':

			r = 3
			print "going right"
			return self.directions[r]


		if self.last_result != 'success' and self.last_direction == 'right' or self.last_direction == 'left':

			r = 2
			print "step down"
			return self.directions[r]

		print "going left"
		return self.directions[r]



	def put_result(self, result):

		self.result = result

		self.last_result = result

	def put_decision(self, decision):

		self.last_direction

