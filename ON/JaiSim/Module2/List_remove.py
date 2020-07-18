Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #del
>>> motorcycles = ['honda','yamaha','suzuki']
>>> del motorcycles[1]
>>> print (motorcycles)
['honda', 'suzuki']
>>> #pop
>>> motorcycles = ['honda','yamaha','suzuki']
>>> popped_motorcycles = motorcycles.pop()
>>> print(motorcycles)
['honda', 'yamaha']
>>> print(popped_motorcycles)
suzuki
>>> first_owned = motorcycles.pop(0)
>>> print("the first motorcycle I owned was a ", first_owned)
the first motorcycle I owned was a  honda
>>> #remove
>>> motorcycles = ['honda','yamaha','suzuki','ducati']
>>> motorcycles.remove('ducati')
>>> print(motorcycles)
['honda', 'yamaha', 'suzuki']
>>> 