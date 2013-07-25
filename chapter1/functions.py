#!/usr/bin/python
#
# Example file for functions
#

def function1():
	print "I'm a function"
	
def function2(arg1, arg2):
	print "I'm a function with ", arg1, arg2
	
def multiargs(*args):
	arguments = "";
	for x in args:
		arguments += x + " "
	print arguments

function1()
function2(2, "arguments")
multiargs("arg 1", "second arg", "third argument")
