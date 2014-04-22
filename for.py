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

print
print "else"

from math import sqrt
for n in range(99, 81, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break
else:
	print "did not find it"

print
print "list comprehension"

y = [x * x for x in range(10)]
print y

print
y = [x * x for x in range(10) if x % 3 == 0]
print y

print
z = [(x, y) for x in range(3) for y in range(3)]
print z

print

girls = ["alice", "kate"]
boys = ["john", "kom"]
print [b+"+"+g for b in boys for g in girls if b[0] == g[0]]

#print
#dictgirls = {}
#for girl in girls:
#	dictgirls.setdefault(girl[0], []).append(girl)
#
#print [b+"+"+g for b in boys for g in dictgirls[b[0]]]
