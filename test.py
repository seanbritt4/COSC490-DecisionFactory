from Stack import *

s = SuperStack()

print 'WASD for directions. Q to quit'

key = ''
while key != 'q':
	key = raw_input()
	key= key.lower()
	if key == 'q':
		pass
	elif key == 'w':
		s.superPush('up')
	elif key == 'a':
		s.superPush('left')
	elif key == 's':
		s.superPush('down')
	elif key == 'd':
		s.superPush('right')

	print s.current_location

		# s.superPush(key)

print "printMoves"
s.printMoves()
print "printDiscovered"
s.printDiscovered()
print "printAll"
s.printAll()

for i in range(0, s.getSize()):
	print s.superPop()


s.printAll()
print s.current_location
'''
using Stack class, can finish OR we can use lists as stacks
	FIFO used in lists
'''
# s = Stack()
# s.printStack()
# s.push('left')

# print
# s.printStack()