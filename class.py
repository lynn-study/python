#!/usr/bin/python

#callable(obj)
#getattr(obj, name[, default])
#hasattr((obj, name)
#isinstance(obj, class)
#issubclass(A, B)
#random.choice(sequence)
#setattr(obj, name, value)
#type(obj)

__mataclass__ = type

class Person:
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def greet(self):
		print "hello" + self.name

foo = Person()
foo.setName("world")
print foo.getName()
foo.greet()

class Class:
	def method(self):
		print "I have a self!"

def function():
	print "I do not..."

instance = Class()
instance.method()
instance.method = function
instance.method()

class Bird:
	song = "qqqqq"
	def sing(self):
		print self.song

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()

class Secretive:
	def __inaccessible(self):
		print "you can not see me..."
	def accsible(self):
		print "you can see me..."
		self.__inaccessible()

s = Secretive()
s.accsible()
s._Secretive__inaccessible() # do not use


class MemberCount:
	members = 0
	def init(self):
		MemberCount.members += 1

m1 = MemberCount()
m1.init()
print m1.members

m2 = MemberCount()
m2.init()
print m2.members

m1.members = 'Two'
print m1.members
print m2.members

class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1, 2, 3])

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'egg', 'apple'])

print issubclass(SPAMFilter, Filter)
print isinstance(s, SPAMFilter) # Do not use

class Calulator:
	def caculate(self, expression):
		self.value = eval(expression)

class Talker:
	def talk(self):
		print "Hi, my value is" , self.value

class TalkingCalculator(Calulator, Talker): # Caculate first
	pass
