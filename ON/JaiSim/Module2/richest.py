Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> income={'Alice':90000,'Bob': 100000,'Apiwat': 999998,'Stark': 999999}
>>> highest = max(income,key=income.get)
>>> print("The richest man on earth:", end= ' ' )
The richest man on earth: 
>>> print(highest + ' with $' + str(income[highest]))
Stark with $999999
>>> 