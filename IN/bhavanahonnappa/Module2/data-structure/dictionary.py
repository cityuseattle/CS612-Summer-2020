#accessing
dict={'Name' : 'abc','Age':7 }
print("Name = ", dict['Name'],"\n", "Age :", dict['Age'])

#updating
dict['Age']= 20
print("updated Age:", dict['Age'])

#adding
dict['phone_no']= 123456789
print("After adding new pair :", dict)

#Deleting
del dict['phone_no']
print("After deleting Phone no :", dict)