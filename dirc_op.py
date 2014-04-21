#!/usr/bin/python

x = {}
x["name"] = "john"
x["age"] = "32"

print "x = " + repr(x)

y = x
print "y = " + repr(y)

x = {}

print "x = " + repr(x)
print "y = " + repr(y)

print

x.clear()
print "x = " + repr(x)
print "y = " + repr(y)

print

x = {"username" : "admin", "machine" : ["foo", "bar", "baz"]}
y = x.copy()
print "x = " + repr(x)
print "y = " + repr(y)

y["username"] = "lynn"
y["machine"].remove("bar")
print "y = " + repr(y)

print

import copy

d = {}
d["names"] = ["john", "kate"]
c = d.copy()
dc = copy.deepcopy(d)
d["names"].append("tom")
print "c = " + repr(c)
print "dc = " + repr(dc)

print

tmp = dict.fromkeys(["name", "age"])
print tmp

tmp = dict.fromkeys(["name", "age"], "unknow")
print tmp

d = tmp.get("name")
print d
x = tmp.get("addr", "N/A")
print x

it = dc.iteritems()
print it

d = {}
d.setdefault("name", "N/A")
print d
d["name"] = "john"
x = d.setdefault("name", "N/A")
print x

d = {"name" : "john"}
print d
e = {"age" : "21"}
d.update(e)
print d

d = {}
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 1

print d.values()
