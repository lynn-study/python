#!/usr/bin/python

class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a + self.b
		return self.a
	def __iter__(self):
		return self

fibs = Fibs()
for f in fibs:
	if f > 1000:
		print f
		break

it = iter([1, 2, 3])
print it.next()
print it.next()

class TestIterator:
	value = 0
	def next(self):
		self.value += 1
		if self.value > 10: raise StopIteration
		return self.value
	def __iter__(self):
		return self

ti = TestIterator()
print list(ti)

def Flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element

nested = [[1, 2], [3, 4], [5]]
for num in Flatten(nested):
	print num

def Flatten(nested):
	try:
		for sublist in nested:
			for element in Flatten(sublist):
				yield element
	except TypeError:
		yield nested

print list(Flatten([[1, 2], [[1], [1, [1, 2]]]]))

def Flatten(nested):
	try:
		try: nested + ''
		except TypeError: pass
		else: raise TypeError
		for sublist in nested:
			for element in Flatten(sublist):
				yield element
	except TypeError:
		yield nested

print list(Flatten([[1, 2], [[1], [1, [1, 2]]]]))
print list(Flatten(['foo', ["haha", "oo"], ["ba"]]))
