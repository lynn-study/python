#!/usr/bin/python

import sys, shelve

def store_person(db):
	"""
	store data in the shelf object
	"""
	pid = raw_input("Enter unique ID number: ")
	person = {}
	person["name"] = raw_input("Enter name: ")
	person["age"] = raw_input("Enter age: ")
	person["phone"] = raw_input("Enter phone: ")

	db[pid] = person

def lookup_person(db):
	"""
	lookup person
	"""

	pid = raw_input("Enter ID number: ")
	filed = raw_input("What would you like to know? (name, age, phone)")
	filed = filed.strip().lower()
	print filed.capitalize() + ":", db[pid][filed]

def enter_cmd():
	cmd = raw_input("Enter command (? for help): ")
	cmd = cmd.strip().lower()
	return cmd

def main():
	database = shelve.open("./database.dat")
	try:
		cmd = enter_cmd()
		if cmd == "store":
			store_person(database)
		elif cmd == "lookup":
			lookup_person(database)
		elif cmd == "quit":
			return
	finally:
		database.close()

if __name__ == '__main__':main()
