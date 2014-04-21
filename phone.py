#!/usr/bin/python

people = {
	"john" : {
		"phone"	: "123",
		"addr"	: "jinzhong road"
	},
	"kate" : {
		"phone" : "234",
		"addr"	: "changning road"
	},
	"tom" : {
		"phone" : "456",
		"addr"	: "minhang road"
	}
}

labels = {
	"phone"	: "phone number",
	"addr"	: "address"
}

name = raw_input("Name ")
name = name.lower()

request = raw_input("Phone number (p) or address (a)")
request = request.lower()

if request == "p" : key = "phone"
if request == "a" : key = "addr"

if name in people : print "%s %s is %s" % (name, labels[key], people[name][key])

#person = person.get(name, {})
#label = labels.get(key, key)
#result = person.get(key, "not available")
