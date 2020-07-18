Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file=open('hello.txt')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    file=open('hello.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'
>>> file = open ('hello.txt')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    file = open ('hello.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'
>>> print(file.read())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(file.read())
NameError: name 'file' is not defined
>>> 