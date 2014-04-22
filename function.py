#!/usr/bin/python

#import math
#x = 1
#y = math.sqrt
#print callable(x) # did not support for python 3.0
#print callable(y) # hasattr(func, __call__) instead of it
#
#print "define a functiong"
#
#def hello(name):
#	return "hello, " + name + "!"
#
#print hello("lynn")
#
#print
#
#def fibs(num):
#	result = [0, 1]
#	for i in xrange(num - 2):
#		result.append(result[-2] + result[-1])
#	return result
#
#num = input("Number: ")
#print fibs(num)
#
#print
#print "Functiong doc"
#
#def square(x):
#	"Calculates the square of x"
#	return x * x
#
#print square.__doc__
#
#print
#
#def inc(x):
#	x[0] = x[0] + 1
#
#i = [10]
#print i
#inc(i)
#print i

#def hello(greet = "hello", name = "world"):
#	print "%s, %s!" % (greet, name)
#
#hello()
#hello(greet = "welcome", name = "lynn")

#def hello_1(name, greeting = "hello", punctuation = "!"):
#	print "%s, %s%s" % (name, greeting, punctuation)
#
#hello_1("lynn")
#hello_1("lynn", "welcome")
#hello_1("lynn", "welcome", "...")

#def print_params_1(*params):
#	print params
#
#print_params_1(1)
#print_params_1(1, 2 ,3)
#
#def print_params_2(title, *params):
#	print title
#	print params
#
#print_params_2("hello", 1, 3, 5)

#def print_params_3(**params):
#	print params
#
#print_params_3(x = 1, y = 2, z = 3)

#def print_params_4(x, y, z = 3, *pospar, **keypar):
#	print x, y, z
#	print pospar
#	print keypar
#
#print_params_4(1, 2, 3, 4, 5, 6, 7, foo = 1, bar = 2)

#def with_stars(**kwds):
#	print kwds["name"] , "is", kwds["age"], "years old"
#
#def without_stars(kwds):
#	print kwds["name"] , "is", kwds["age"], "years old"
#
#args = {"name" : "kate", "age" : 43}
#with_stars(**args)
#without_stars(args)

#def story(**kwds):
#	return "Once upon a time, there was a " \
#		"%(job)s called %(name)s" % kwds
#
#print story(job = "king", name = "gumby")
#print story(name = "gumby", job = "king")
#params = {"name" : "gumby", "job" : "king"}
#print story(**params)
#del params["job"]
#print story(job = "driver", **params)

extern = "extern"

def combine(para):
	print para + globals()["extern"]

combine("hello")

print

def change_global():
	global x
	x = x + 1

x = 1
change_global()
print x
