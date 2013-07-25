#!/usr/bin/python
#
# Example file for global Variables
#

f = 0;
print f # prints 0

def someFunction():
	global f
	f = "def"
	print f # prints def
	
someFunction()
print f # prints 0

