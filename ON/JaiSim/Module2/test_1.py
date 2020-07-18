Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
	fh=open("testfile","w")
	fh.write("this is ,y test file for exception handling")
except IOError:
	print("Error: cant\'t find file or read data")
else:
	print("Written content in the file sucessfully")
	fh.close()

	
43
Written content in the file sucessfully
>>> 