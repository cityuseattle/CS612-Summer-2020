# accessing
dict = {'Name': 'abc', 'Age': 7}
print("Name: ", dict['Name'], "\n", "Age:", dict['Age'])

# update
dict['Age'] = 20
print("Updated Age:", dict['Age'])

# adding
dict['Phone_no'] = 123456789
print("After adding the new pair:", dict)

# deleting
del dict['Phone_no']
print("After deleting phone_no:", dict)