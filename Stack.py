'''
	incomplete BUT can finish if wanted/needed
	
	also have you guys seen the spice girls lately. i kinda hoped one of them were looking rough but they all held up pretty well. good for them.
'''
'''
class Stack:
	def __init__(self):
		# self.head_node = Node(0,0)
		print 'stack init'
		self.head_node = Node('none')
		# print "in: ", self.head_node


	def push(self, direction):
		print 'stack push'
		new_node = Node(direction)
		# print new_node
		new_node.printNode()

		node = self.head_node
		while node.next_node:
			node = node.next_node
			# print "push while: ", node

		node.next_node = new_node


	def pop(self):
		print 'stack pop'
		pass


	def printStack(self):
		print 'stack print'
		node = self.head_node
		while node:
			node.printNode()
			# print node
			# print node.next_node
			node = node.next_node
'''
class easyStack():
	def __init__(self):
		self.moves = []
		self.discovered = []
		self.current_location = [0,0]
		self.size = 0

	def easyPop(self):
		return self.moves.pop()

	def easyPush(self, move):
		self.size += 1
		self.moves.append(self.toCoord(move))
		self.discovered.append(move)

	def toCoord(self, move):
		if move == 'up':
			self.current_location[1] -= 1
		if move == 'down':
			self.current_location[1] += 1
		elif move == 'left':
			self.current_location[0] -= 1
		elif move == 'right':
			self.current_location[0] += 1

		return self.current_location

	def getSize(self):
		return self.size


	'''
		print functions used for debugging
	'''
	def printMoves(self):
		print self.moves

	def printDiscovered(self):
		print self.discovered

	def printAll(self):
		print "Moves:"
		print self.moves
		print "Discovered"
		print self.discovered