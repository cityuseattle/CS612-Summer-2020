dict={'name':'abc','age':7}
print("name:",dict['name'],"\n","age :",dict['age'])

dict['age']=20
print("updated age", dict['age'])

dict['phone']=123456
print("after adding the phone", dict)

del dict['phone']
print("after deleting phonr", dict)