from Stack import *

s = easyStack()

print 'WASD for directions. Q to quit'

key = ''
while key != 'q':
	key = raw_input()
	key= key.lower()
	if key == 'q':
		pass
	elif key == 'w':
		s.easyPush('up')
	elif key == 'a':
		s.easyPush('left')
	elif key == 's':
		s.easyPush('down')
	elif key == 'd':
		s.easyPush('right')

	print s.current_location

		# s.easyPush(key)

print "printMoves"
s.printMoves()
print "printDiscovered"
s.printDiscovered()
print "printAll"
s.printAll()

for i in range(0, s.getSize()):
	print s.easyPop()


s.printAll()
'''
using Stack class, can finish OR we can use lists as stacks
	FIFO used in lists
'''
# s = Stack()
# s.printStack()
# s.push('left')

# print
# s.printStack()