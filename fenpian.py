#!/usr/bin/python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print numbers[3:6]

print numbers[-3:-1]

print numbers[-3:]

print numbers[:3]

print numbers[:]

print numbers[0:10:3]

perssion = "rw"

x = "w" in perssion
print x

users = ["mlh", "foo", "haha"]
x = raw_input("Enter your name: ") in users
print x
