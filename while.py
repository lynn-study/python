#!/usr/bin/python

x = 1
while x <= 100:
	print x
	x += 1

name = ""
while not name.strip():
	name = raw_input("Name:")
print name

while True:
	word = raw_input("Enter words:")
	if word:
		break
print word
