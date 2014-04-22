#!/usr/bin/python

Exception
AttributeError
IOError
IndexError
KeyError
NameError
SyntaxError
TypeError
ValueError
ZeroDivisionError

raise Exception
raise Exception('down')

class SomeCustomException(Exception):
	pass

try:
	x = input('x: ')
	y = input('y: ')
	print x / y
except ZeroDivisionError:
	print "y can not be zeor!"
except TypeError:
	print "That was not a number"

try:
	x = input('x: ')
	y = input('y: ')
	print x / y
except (ZeroDivisionError, TypeError, NameError), e:
	print e

try:
	x = input('x: ')
	y = input('y: ')
	print x / y
except:
	print "something wrong"

class MuffledCalcultator:
	muffled = False
	def calc(self, expr):
		try:
			return eval(expr)
		except ZeroDivisionError:
			if self.muffled:
				print 'Division by zero is illegal'
			else:
				raise

try:
	print "go on"
except:
	print "something wrong"
else:
	print "keep going"

while True:
	try:
		x = input("x:")
		y = input("y:")
		value = x / y
		print "x / y = ", value
	except:
		print "invalid input! input again"
	else:
		break

x = None
try:
	x = 1 / 0
finally:
	print "Clean up..."
	del x

try:
	1 / 0
except NameError:
	print "Unknown variable"
else:
	print "that went well!"
finally:
	print "Clean up..."

def decribeperson(person):
	print "decription" , person['name']
	print "Age", person['age']
	try:
		print "occu:" + person['occu']
	except KeyError: pass

try:
	obj.write
except AttributeError:
	print "unable to write"
else:
	print "writeable"
