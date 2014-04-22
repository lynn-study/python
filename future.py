#!/usr/bin/python

class FooBar:
	def __init__(self, value = 8):
		self.var = value
	def __del__(self): #Do not use
		pass

a = FooBar()
print a.var

b = FooBar('Hello')
print b.var

print

class A:
	def hello(self):
		print "hello"
class B(A):
	def hello(self):
		print "I am b"
a = A()
a.hello()
b = B()
b.hello()

class Bird():
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print "aaaa"
		else:
			print "no full"
class SongBird(Bird):
	def __init__(self):
		Bird.__init__(self)
		self.sound = "squawk"
	def sing(self):
		print self.sound

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

__metaclass__ = type

class Bird():
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print "aaaa"
		else:
			print "no full"
class SongBird(Bird):
	def __init__(self):
		super(SongBird, self).__init__()
		self.sound = "squawk"
	def sing(self):
		print self.sound

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
