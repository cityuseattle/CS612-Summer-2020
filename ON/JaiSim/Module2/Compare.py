Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #compare two list
>>> first = ['cats','dogs']
>>> second = ['dogs',55,'cats']
>>> print(first==second)
False
>>> #compare two dictionary, order does not matter
>>> first_dict={'name':'aaa','species': 'human', 'age': 20}
>>> second_dict ={'species': 'human','age':20, 'name': 'aaa'}
>>> print(first_dict==second_dict)
True
>>> 