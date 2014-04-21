#!/usr/bin/python

import math
from cmath import sqrt

x = math.floor(21.9)
print x

y = int(math.floor(21.9))
print y

z = sqrt(-1)
print z

w = (1 + 3j) * (2 + 4J)
print w

# import somemoudle

# from somemoudle import somefunction

# from somemoudle import somefunction anothersomefunction yetanothersomefunction

# from somemoudle import *

import math as foobar

foobar.sqrt(4)

from math import sqrt as foobar
foobar(4)
