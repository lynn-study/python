#!/usr/bin/python
#
#database = [
#        ['jhon', '123'],
#        ['helen', '345'],
#        ['suny', '987'],
#        ['yoko', '313']
#]
#
#username = raw_input('input your name: ')
#pin= raw_input('input your password: ')
#
#if [username, pin] in database: print 'Access granted'
#
#name = raw_input("Enter name: ")
#if name.endswith("lynn"):
#	print "hello lynn"
#else:
#	print "I do not know who you are"

#num = input("Enter num: ")
#if num > 0:
#	print "num > 0"
#elif num < 0:
#	print "num < 0"
#else:
#	print "num == 0"

name = raw_input("Name:")
if name.endswith("lynn"):
	if name.startswith("mr"):
		print "hello Mr Lynn"
	elif name.startswith("mrs"):
		print "hello Mrs Lynn"
	else:
		print "hello Lynn"
else:
	print "hello stranger"
