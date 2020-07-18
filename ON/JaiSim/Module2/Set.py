Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #joining two sets
>>> set1 = {"a","b","c"}
>>> set2 = {1,2,3}
>>> set3 = set1.union(set2)
>>> print(set3)
{1, 2, 3, 'a', 'b', 'c'}
>>> set1.update(set2)
>>> print(set1)
{1, 2, 3, 'a', 'b', 'c'}
>>> #constructor
>>> thisset = set(("apple","banana","cherry"))#note the double round-brackets
>>> print(thisset)
{'apple', 'cherry', 'banana'}
>>> 