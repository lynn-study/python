#!/usr/bin/python

import copy

print [n for n in dir(copy) if not n.startswith('_')]

print

#print copy.__all__

print

#help(copy.copy)
print

#print copy.copy.__doc__
