Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file = open('hello.txt','a')
>>> file.write('\nThis is new content I just appended')
36
>>> file.close()
>>> new_file = open('world.txt','w')
>>> new_file.write('this is new file')
16
>>> new_file.close()
>>> file = open('hello.txt')
>>> content = file.read()
>>> file.close()
>>> print(content)

This is new content I just appended
>>> 