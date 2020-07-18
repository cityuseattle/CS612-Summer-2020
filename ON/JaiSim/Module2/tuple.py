Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> courses = ('CS101',2.0,3)
>>> courses[1] = 4.0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    courses[1] = 4.0
TypeError: 'tuple' object does not support item assignment
>>> 