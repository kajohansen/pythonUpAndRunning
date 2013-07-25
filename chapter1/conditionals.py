#!/usr/bin/python
#
# Example file for conditionals
#

x = 10
y = 100
z = 1000

if z < y:
	print "z is less than y"
elif y > z:
	print "y is greater than z"
else:
	print "no previous conditions where met"
	
st = "x is less than y" if x < y else "x is greater than y"
print st