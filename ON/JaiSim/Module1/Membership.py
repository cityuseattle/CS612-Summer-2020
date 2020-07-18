Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> list = [1,2,3,4,5]
>>> if (a in list ):
	print("Line 1 - a is available in the given list")
else:
	print("Line 1 - a is not available in the given list")
if (b not in list ):
	
SyntaxError: invalid syntax
>>> if ( b not in list ):
	print("Line 2 - b is not available in the fiven list")
else:
	print("Line 2 - b is available in the given list")

	
Line 2 - b is not available in the fiven list
>>> a=2
>>> if ( a in list ):
	print ("Line 3 - a is available in the given list")

	
Line 3 - a is available in the given list
>>> else:
	
SyntaxError: invalid syntax
>>> else
SyntaxError: invalid syntax
>>> a=2
>>> if ( a in list ):
	print ("Line 3 - a is available in the given list")
else:
	print ("Line 3 - a is not available in the given list")

	
Line 3 - a is available in the given list
>>> 