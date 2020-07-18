Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def number(limit):
	i=0
	numbers = []
	while i<limit:
		numbers.append(i)
		i=i+1
	return numbers

>>> user_limit = int(input("Give a limit"))
Give a limit3
>>> print(numbers(user_limit))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(numbers(user_limit))
NameError: name 'numbers' is not defined
>>> 