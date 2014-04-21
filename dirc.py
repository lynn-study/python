#!/usr/bin/python

phonebook = {"Tom" : "234", "John" : "335", "kate" : "353"}

print phonebook["Tom"]

items = [("name", "John"), ("age", 32)]
print items[1]
d = dict(items)
print d
print d["name"]

print

print len(d)

print d["name"]

d["name"] = 11
print d["name"]

if "name" in d: print "found it"

del d["name"]

print

obj = dict(name = "Kate", age = 18)
print obj

print

#bad
#x = []
#x[42] = "foobar"

x = {}
x[42] = "foobar"
print x

print "Tom number is %(Tom)s" % phonebook
