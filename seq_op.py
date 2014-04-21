#!/usr/bin/python

x = [1, 2, 3]
print x

print

x[1] = 4

print x

print

del x[1]

print x

print

name = list('perl')
print name

name[2:] = list('ar')
print name

name_1 = list('perl')
print name_1

name_1[1:] = list('ython')
print name_1

print

numbers = [1, 5]
print numbers

numbers[1:1] = [2, 3, 4]
print numbers

numbers[1:4] = []
#del numbers[1:4]

print numbers

print

price = [1, 2, 3, 4, 4, 3, 2, 1]
print price
price.append(5)
print price

print

i = price.count(1)
print i

print

a = [1, 2, 3]
b = [3, 2, 1]

a.extend(b)
print 'a.extend(b) = ' + repr(a)
# a = a + b slow
# a[len(a):] = b hard to see

print

name = ['john', 'lily', 'lucy', 'kate']
num = name.index('lucy')
print num

print

print name
name.insert(2,'lilei')
print name

name.pop()
print name
name.pop(0)
print name

x = [1, 2, 3]
print x
x.append(x.pop())
print x

print
x = ["bl", "be", "bl"]
print x
x.remove('bl')
print x

print
x = [1, 2, 3]
print x
x.reverse()
print x
print list(reversed(x))

print
x = [1, 99, 34, 56, 97]
y = x[:]
print x
x.sort()
y.sort()
print x
print y

y = sorted(x)
print y
y.reverse()
print y

x = ["aardvard", "abalone", "acme", "aerate"]
print x
x.sort(key=len)
print x

x = [1, 99, 34, 56, 97]
print x
x.sort(reverse=True)
print x
