Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def printme( str ):
	print (str)
	return
#now you can call printme function
printme("First call to user defined function!")
SyntaxError: invalid syntax
>>> printme("Second call to the same function")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    printme("Second call to the same function")
NameError: name 'printme' is not defined
>>> 