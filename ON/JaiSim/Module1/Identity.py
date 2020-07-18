Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=20
>>> b=20
>>> if ( a is b ):
	print ("Line 1 - a and b have same identity")
else:
	print ("Line 1 - a and b do not have same identity")

	
Line 1 - a and b have same identity
>>> if ( id(a) == id(b) ):
	print ("Line 2 - a and b have same identity")
else:
	print ("Line 2 - a and b do not have same identity")

	
Line 2 - a and b have same identity
>>> b=30
>>> if ( a is b ):
	print ("Line 3 - a and b have same identity")
else:
	print ("Line 3 - a and b do not have same identity")

	
Line 3 - a and b do not have same identity
>>> if (a is not b ):
	print ("Line 4 - a and b do not have same identity")
else:
	print ("Line 4 - a and b have same identity")

	
Line 4 - a and b do not have same identity
>>> 