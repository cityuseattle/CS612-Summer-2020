dict = {'Name':'abc','Age':7}
print("name :",dict['Name'], "\n","age :",dict["Age"])

dict["Age"] = 20
print("updated age :",dict['Age'])

dict["phone"] = 123456789
print("After adding the new pair:",dict)

del dict["phone"]
print("after deleting phone:",dict)