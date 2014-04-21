#!/usr/bin/python

width = input("input width: ")

price_width = 10
item_width = width - price_width

header_format	= "%-*s%*s"
format		= "%-*s%*.2f"

print header_format % (item_width, "Item", price_width, "Price")

print "-" * width

print format % (item_width, "apple", price_width, 4.5)
print format % (item_width, "banane", price_width, 45.3)
print format % (item_width, "pea", price_width, 14.5)
print format % (item_width, "peak", price_width, 44.5)
