#!/usr/bin/python

# r w x b a t u +

# stdin stdout stderr

import sys, fileinput

def process(string):
	print "Processing: " + string

#text = sys.stdin.read()
#print text

#for line in sys.stdin:
#	process(line)


fd = open('/home/x/work/study/python/data.txt', 'ra+')
fd.write("1234567890")
text = fd.read(2)
print text
fd.seek(5)
text = fd.read(4)
print text
print fd.tell()
fd.close()

print

fd = open('/home/x/work/study/python/test.txt', 'ra+')
fd.write("1\n2\n3\n4\n5\n6\n7890")
fd.close()
fd = open('/home/x/work/study/python/test.txt', 'ra+')
line = fd.readline(4)
print line
fd.close()

fd = open('/home/x/work/study/python/test.txt', 'ra+')
while True:
	char = fd.read(1)
	if not char: break
	process(char)
fd.close()

fd = open('/home/x/work/study/python/test.txt', 'ra+')
while True:
	line = fd.readline()
	if not line: break
	process(line)
fd.close()

fd = open('/home/x/work/study/python/test.txt', 'ra+')
for char in fd.read():
	process(char)
fd.close()

fd = open('/home/x/work/study/python/test.txt', 'ra+')
for line in fd.readlines():
	process(line)
fd.close()

for line in fileinput.input('/home/x/work/study/python/test.txt'):
	process(line)


fd = open('/home/x/work/study/python/test.txt')
for line in fd:
	process(line)
fd.close()

for line in open('/home/x/work/study/python/test.txt'):
	process(line)

lines = list(open('/home/x/work/study/python/test.txt'))
print lines

with open('/home/x/work/study/python/test.txt') as fd:
	for line in fd:
		print line
