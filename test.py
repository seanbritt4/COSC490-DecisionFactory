import re

s = "map00.txt"

x = re.search("map.*\.txt", s)

if x:
	print x.string
else:
	print 'Not Found'
