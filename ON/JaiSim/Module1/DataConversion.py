Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> price = 10
>>> print("how many beers you want?")
how many beers you want?
>>> print("Your total price is: $" + priced * input())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("Your total price is: $" + priced * input())
NameError: name 'priced' is not defined
>>> price = 10
>>> input=int("# of beers?")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    input=int("# of beers?")
ValueError: invalid literal for int() with base 10: '# of beers?'
>>> price = 10
>>> 