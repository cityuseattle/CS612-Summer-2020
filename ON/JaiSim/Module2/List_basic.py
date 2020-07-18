Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = ['physics','chemistry',1997,2000]
>>> list2 = [1,2,3,4,5,6,7]
>>> print("list1[0]:", list1[0])
list1[0]: physics
>>> print("list2[1:5]:", list2[1:5])
list2[1:5]: [2, 3, 4, 5]
>>> #updating
>>> print("value available at index 2: ")
value available at index 2: 
>>> print(list1[2])
1997
>>> list1[2]=2001
>>> print("New value available at index 2 : ")
New value available at index 2 : 
>>> print (list1[2])
2001
>>> #adding
>>> list1.append(2020)
>>> print("New ListL" , list1)
New ListL ['physics', 'chemistry', 2001, 2000, 2020]
>>> #insert
>>> list1.insert(0,'python')
>>> print("after inserting: ", list1)
after inserting:  ['python', 'physics', 'chemistry', 2001, 2000, 2020]
>>> 