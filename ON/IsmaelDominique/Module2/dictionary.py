#Accessing
dict = {'Name': 'abc','Age': 7}
print ("Nmae :", dict['Name'] , "\n" , "Age :", dict['Age'])

#updating
dict['Age']= 20
print("Updating age :" , dict['Age'])

#Adding
dict['Phone_no']= 123456789
print("After adding the new pair :", dict)

#Deleting
del dict['Phone_no']
print("After delecting phone_no :" , dict)
