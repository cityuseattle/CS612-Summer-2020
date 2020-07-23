#accessing
dict = {'name': 'abc', 'age': 7}
print('name : ', dict['name'], '\n', 'age : ', dict['age'])

#updating
dict['age'] = 20
print('updated age : ', dict['age'])

#adding
dict['phone_no'] = 123456789
print("after adding the new pair : ", dict)

#deleting
del dict['phone_no']
print('after deleting phone_no : ', dict)