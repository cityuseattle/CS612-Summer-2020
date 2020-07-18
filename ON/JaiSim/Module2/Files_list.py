Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> filename='hello.txt'
>>> with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())

		

This is new content I just appended
>>> 