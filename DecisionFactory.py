import random
#import numpy as np

class DecisionFactory:
	def init(self, name='Davros'):
		self.name = name
		self.directions = ['wait', 'up', 'down', 'right', 'left']
		self.lastresult = 'success'
		self.lastdirection = 'wait'

	#Note: we have relativistic coordinates recorded here, since the map
	# is relative to the player's sfirst known and recorded position:
	#self.state.pos = (0,0)

	def getdirection(self, verbose = True):
		return self.randomdirection()

	def randomdirection(self):
		#random.randint(0,4) #Includes wait state
		r = random.randint(1,4) #Does NOT include wait state

		self.lastdirection = self.directions[r]
		return self.directions[r]

	def putresult(self, result):
		self.last.result = result
