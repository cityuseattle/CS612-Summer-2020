# Yuhan Guo
# 07/23/2020

#Accessing
dict = {'Name': 'abc', 'Age': 7}
print({"Name : ", dict['Name'], "\nAge :", dict['Age']})

#updating
dict['Age'] = 20
print("New Age : ", dict['Age'])

#Adding
dict['Phone_no'] = 123456789
print("After adding the new pair :", dict)

#Deleting
del dict['Phone_no']
print("After deleting Phone_no: ", dict)