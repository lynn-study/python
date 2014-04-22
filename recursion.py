#!/usr/bin/python

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

print factorial(5)

def power(x, n):
	if n == 0:
		return 1
	else:
		return x * power(x, n - 1)

print power(5, 2)

def finds(sequence, number, lower, upper):
	if lower == upper:
		assert number == sequence[upper]
		return upper
	else:
		middle = (lower + upper) // 2
		if number > sequence[middle]:
			return finds(sequence, number, middle + 1, upper)
		else:
			return finds(sequence, number, lower, middle)

seq = [12, 345, 4646, 23, 5646, 35]
seq.sort()
print seq

ret = finds(seq, 35, 0, 5)
print ret
