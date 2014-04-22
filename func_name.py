#!/usr/bin/python

def init(data):
	data["first"] = {}
	data["middle"] = {}
	data["last"] = {}

def loolup(data, label, name):
	return data[label].get(name)

def store(data, full_name):
	names = full_name.split()
	if len(names) == 2:
		names.insert(1, "")
	labels = ("first", "middle", "last")
	for label, name in zip(labels, names):
		people = loolup(data, label, name)
		if people:
			people.append(full_name)
		else:
			data[label][name] = [full_name]

def stores(data, *full_names):
	for full_name in full_names:
		names = full_name.split()
		if len(names) == 2:
			names.insert(1, "")
		labels = ("first", "middle", "last")
		for label, name in zip(labels, names):
			people = loolup(data, label, name)
			if people:
				people.append(full_name)
			else:
				data[label][name] = [full_name]

myname = {}
init(myname)
#store(myname, "john stevog o")
store(myname, "john stevog")
stores(myname, "john haha", "nike hdle dig", "diejf dkgld gid")
tmp = loolup(myname, "first", "john")
print tmp
tmp = loolup(myname, "first", "nike")
print tmp
tmp = loolup(myname, "first", "diejf")
print tmp
