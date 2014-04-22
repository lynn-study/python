#!/usr/bin/python

def checkIndex(key):
	if not isinstance(key, (int , long)): raise TypeError
	if key < 0: raise IndexError

class ArithmeticSequence:
	def __init__(self, start = 0, step = 1):
		self.start = start
		self.step = step
		self.changed = {}
	def __getitem__(self, key):
		checkIndex(key)
		try: return self.changed[key]
		except KeyError:
			return self.start + key * self.step

	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key] = value

s = ArithmeticSequence(1, 2)
print s[4]
s[4] = 2
print s[4]
print s[5]

print

class CounterList(list):
	def __init__(self, *args):
		super(CounterList, self).__init__(*args)
		self.count = 0
	def __getitem__(self, index):
		self.count += 1
		return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print cl
tmp = cl.reverse()
print tmp
del cl[3:6]

__metaclass__ = type

class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
	def SetSize(self, size):
		self.width , self.height = size
	def GetSize(self):
		return self.width, self.height

	size = property(GetSize, SetSize)

r = Rectangle()
r.width = 10
r.height = 20
print r.size
r.size = 100, 200
print r.width
print r.height
