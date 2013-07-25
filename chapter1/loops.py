#!/usr/bin/python
#
# Example file for loops
#

x = 0;

print "while loop"
while x < 5:
	print x
	x += 1
	
print "for loop"
for x in range(5, 10):
	print x
	
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
	print i, d
