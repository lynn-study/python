#!/usr/bin/python

print "hello"
print

x = "hello,"
y = "shuai"

print x + y
print

print "one" + "two"
print

print repr("hello, world!")
print repr("10000L")
print

print str("hello, world!")
print str("10000L")
print

temp = 42
print "the temp is " + `temp`
print
print "the temp is " + repr(temp) #Recommond

print
print """hello
hello
hello"""

print
print "hello, \
world"

print
print "hello,\nworld"
print "hello,\\nworld"

print
print r'c:\nowhere'
print
print u'unicode' #Unicode string

print "age: ", 42

name = "john"
age = "32"
print name, age

print name + ",", age

print

format ="hello, %s and %s ?"
values = ("John", "Tom")

print format % values

format = "pi = %.4f"
from math import pi
print format % pi

#from string import Template
#s = Template("$x, glorious $x!")
#s.substitute(x = "hello")

print "price of eggs $%d" % 42

print "pi = %f" % pi

print "pi = %d" % pi

print "str : %s" % 42L

print "rpr : %r" % 42L

print

print "%10f" % pi
print

print "%10.3f" % pi
print

print "%-10.3f" % pi
print

print "%010.3f" % pi
print

print "%.4f" % pi
print

print "%.5s" % "hello everybody"
print

print "%.*s" % (7, "hello everybody")
print

print ("% 5d" % 10) + "\n" + ("% 5d" % -10)
print ("%+5d" % 10) + "\n" + ("%+5d" % -10)
