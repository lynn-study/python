#!/usr/bin/python

words = ["this", "is", "a", "book"]
for word in words:
	print word

for num in range(10):
	print num

d = {"x" : 1, "y" : 2, "z" : 4}
for key in d:
	print key, "corresponds to", d[key]

for key, value in d.items():
	print key, value

names = ["anne", "john", "kate", "tom"]
ages = ["12", "23", "22", "29"]

for i in range(len(names)):
	print "name:", names[i], "age:", ages[i]

lst = zip(names, ages)
print lst

for name, age in zip(names, ages):
	print name, age

lst = zip(range(5), xrange(10000))
print lst

print

strings = ["this", "is", "a", "book"]
print strings
for index, string in enumerate(strings):
	if "book" in string:
		strings[index] = "apple"
print strings
