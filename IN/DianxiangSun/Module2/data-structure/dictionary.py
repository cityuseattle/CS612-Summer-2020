dict={'name':'abc','Age':7}
print("name:",dict['name'],"\n","Age :",dict['Age'])

dict['Age']=20
print("updated Age", dict['Age'])

dict['phone']=123456
print("after adding the phone", dict)

del dict['phone']
print("after deleting phonr", dict)