import sys

for arg in sys.argv:
	#print arg
	if arg == '-ng' or arg == '-noGraphics':
		print 'no grphics'
	elif arg == "-initOverride" or arg == "-r":
		print 'over ride'
	elif arg == "-fast" or arg == "-f":
		print 'gotta go fast'

