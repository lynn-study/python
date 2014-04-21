#!/usr/bin/python

#x == y
#x < y
#x > y
#x <= y
#x >= y
#x !=y
#x is y
#x is not y
#x in y
#x not in y
#
#0<age<100

print "foo" == "foo"

x = y = [1, 2, 3]
z = [1, 2, 3]

print x == y
print x == z

print x is y

print z is y # False

# if "s" in name;

print "alpha" < "beta"

print "Forld".lower() == "forld".lower()

print [1, 3] < [2, 1]

print [1, [2, 4]] < [2, [1, 5]]

num = input("Enter num")
if num <= 10 and num >=0:
	print "great"
else:
	print "bad"

if 0 <= num <= 10 :
	print "great"
else:
	print "bad"

# if ((cash > price) or customer_rich) and not out_of stock:
# a if b else c
