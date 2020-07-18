Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("this program will sum of numbers from 1 to a number you enter")
this program will sum of numbers from 1 to a number you enter
>>> print("please enter a ending number")
please enter a ending number
>>> num = int (input())
total = 0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    num = int (input())
ValueError: invalid literal for int() with base 10: 'total = 0'
>>> num = int(input("please enter a ending number")
	  total=0
	  
SyntaxError: invalid syntax
>>> num = int(input("please enter a ending number")

	  100
	  
SyntaxError: invalid syntax
>>> while num >=1:
	total +=num
	num -=1

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    while num >=1:
NameError: name 'num' is not defined
>>> 