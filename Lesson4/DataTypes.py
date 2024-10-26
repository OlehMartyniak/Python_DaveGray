# String data types

# literal assignment 
first = 'Oleh'
last = 'Mart'

print(type(first))
# <class 'str'>
print(type(first) == str)
# true
print(isinstance(first,str))
# true

# constructor functions 
pizza = str('Pepperoni')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza,str))

# concatination
fullname = first + ' ' + last
print(fullname)

fullname += '!'
print(fullname)

# casting a number to a string
decade = str(1980)

statement = 'I like rock music from the ' + decade + 's.'
print(statement)

# escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
print(first.upper()) 
print(first.lower())

print(statement.title())
print(statement.replace("1980s","2000s"))
print(len(statement))
print("")

# Build a menu
title = 'menu'.upper()
print(title.center(20,"="))
# ========MENU========

print('Coffe'.ljust(16,'.') + '1$'.rjust(4))
print('Muffin'.ljust(16,'.') + '2$'.rjust(4))
print('Cheesecake'.ljust(16,'.') + '1$'.rjust(4))
# Coffe...........  1$
# Muffin..........  2$
# Cheesecake......  1$



# string index values

# returns the 2nd index
print(first[1])
# returns the last index
print(first[-1])
# returns the range
print(first[1:])
print("")

# some methods return boolean data (True / False)
print(first.startswith('O'))
print(first.endswith('Z'))
print("")

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
print("")
# built-in functions for numbers

gpa = 3.28

print(abs(gpa))
# 3.28
print(round(gpa))
# 3
print(round(gpa,1))
# 3.3

import math
print(math.sqrt(64))
# 8.0
print(math.ceil(gpa))
# 4
print(math.floor(gpa))
# 3
