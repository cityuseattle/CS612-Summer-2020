Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #accessing
>>> dict={'Name':'abc', 'age': 7}
>>> print("Name : " , dict['Name'],"\n", "age :" , dict['Age'])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("Name : " , dict['Name'],"\n", "age :" , dict['Age'])
KeyError: 'Age'
>>> #updating
>>> dict['Age'] = 20
>>> print("Updated age: , dict['Age'])
      
SyntaxError: EOL while scanning string literal
>>> #adding
>>> dict['Phone_no']=123456789
>>> print("After adding the new pair: ", dict)
After adding the new pair:  {'Name': 'abc', 'age': 7, 'Age': 20, 'Phone_no': 123456789}
>>> "deleting
SyntaxError: EOL while scanning string literal
>>> #deleting
>>> del dict['Phone_no']
>>> print("after deleting phone_no:", dict)
after deleting phone_no: {'Name': 'abc', 'age': 7, 'Age': 20}
>>> 