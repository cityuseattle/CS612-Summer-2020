#Accessing
print("Accessing")
dict = {'Name': 'abc', 'Age': 7 }
print("Name: ", dict['Name'], "\n" , "Age: ", dict['Age'])

#updating
print("Updating")
dict['Age'] = 20
print("Updated Age : ", dict['Age'])

#Adding
print("Adding")
dict['Phone_no']=123456789
print("After adding the new pair :", dict)

#Deleting
print("Deleting")
del dict['Phone_no']
print("After deleting phone_no: ", dict)