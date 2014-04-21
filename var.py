#!/usr/bin/python

x, y, z = 1, 2 ,3

print x, y, z

x, y = y, x

print x, y, z

print

dic = {"name" : "john", "age" : "21"}
key, val = dic.popitem()
print key, val

print

# support by python 3.0
#a, b, *rest = [1, 2, 3, 4, 5]
#print a, b, rest

#x = y = somefunction()

x = 2
x += 1
x *= 2
print x

print

fnord = "foo"
fnord += "bar"
fnord *= 2
print fnord
