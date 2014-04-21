#!/usr/bin/python

database = [
	["albert", "1234"],
	["whaha", "1234"],
	["lynn", "1234"],
	["xxxx", "1234"]
]

usrname = raw_input("Enter your name: ")
password = raw_input("Enter your password: ")

if [usrname, password] in database: print "access granted"
