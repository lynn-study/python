#!/usr/bin/python

#find

title = "I like python, it so cool!"
print title.find("like")
print title.find("thon")
print title.find("x")
print title.find("x")

print

print title.find("th", 2)
print title.find("th", 2, 10)

seq = ["1", "2", "3"]
sep = "+"
print seq
print sep

print sep.join(seq)

dirs = "", "usr", "bin", "env"

print "/".join(dirs)

print

print "C:" + "\\".join(dirs)

str = "HELLO"
print str.lower()

name = "John"

names = ["john", "tom"]

if name.lower() in names: print "found it"

str = "this is a apple"
print str
tmp = str.replace("this", "that")
print tmp

str = "1+2+3+4"
print str
tmp = str.split("+")
print tmp

str = "we are happy"
print str
tmp = str.split()
print tmp

str = "     hello      "
print str
tmp = str.strip()
print tmp

str = "****     hello      !!!!"
print str
tmp = str.strip(" *!")
print tmp

print

from string import maketrans

table = maketrans("az", "oO")
print "aaaaaaaaaaaaaaooooooooooo".translate(table, "")
