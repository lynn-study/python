#!/usr/bin/python

1, 2, 3

(1, 2, 3)

()

(66,)

x = 3 * (66,)
print x

lst = [1, 2, 3]
print lst
y = tuple(lst)
print y

print tuple("abcde")

x = tuple("abcdefghi")
print x[1]
print x[1:5]
print x[1:5:2]
