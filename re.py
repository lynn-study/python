#!/usr/bin/python

import re, fileinput

#compile(pattern[, flags])
#search(pattern, string[, flags])
#match(pattern, string[, flags)
#split(pattern, string[, flags])
#findall(pattern, string)
#sub(pattern, replace, string[, count=0])
#escape(string)

some_text = "alpha, beta,,,, gama delta"
res = re.split("[,]+", some_text)
print res

pat = "[A-Za-z]+"
text = "hello how are you?"
res = re.findall(pat, text)
print res

pat = r"[.?\-\",]+"
res = re.findall(pat, text)
print res

pat = "name"
text = "Dear name..."
res = re.sub(pat, "Mr. Gumby", text)
print res

res = re.escape("www.python.org")
print res

text = "www.python.org"
m = re.match(r"www\.(.*)\..{3}", text)
print m.group(1)
print m.start(1)
print m.end(1)
print m.span(1)

emphasis_pattern = re.compile(r"\*([^\*]+)\*", re.VERBOSE)
res = re.sub(emphasis_pattern, r"<em>\1<em>", "Hello, *World*!")
print res

text = "**this** is **it**!"
emphasis_pattern = re.compile(r"\*\*(.+)\*\*", re.VERBOSE) #greedy
res = re.sub(emphasis_pattern, r"<em>\1<em>", text)
print res

emphasis_pattern = re.compile(r"\*\*(.+?)\*\*", re.VERBOSE)
res = re.sub(emphasis_pattern, r"<em>\1<em>", text)
print res

#find email
pattern = re.compile("[a-z\-\.]+@[a-z\-\.]+", re.IGNORECASE)
addresses = set()

for line in fileinput.input():
	for address in pattern.findall(line):
		addresses.add(address)
for address in sorted(addresses):
	print address
