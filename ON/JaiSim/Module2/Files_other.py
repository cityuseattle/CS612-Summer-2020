Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> with open('hello.txt') as file_object:
	contents = file_object.read()
	print(contents)

	
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    with open('hello.txt') as file_object:
FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'
>>> 