Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
	fh = open("testfile","w")
	try:
		fh.write("this is my test file for exception handling!!")
		raise IOError
	finally:
		print("going to close the file")
	except IOError:
		
SyntaxError: invalid syntax
>>> 