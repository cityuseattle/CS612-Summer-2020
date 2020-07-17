list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print ("List1[0]: ", list1[0])
print ("List2[1:5]: ", list2[1:5])

#Updating
print ("Value available at index 2: ")
print (list1[2])
list1[2] = 20001
print ("New value available at index 2: ")
print (list1[2])
list1[2] = 2001
print ("New value available at index 2: ")
print (list1[2])

#Adding 
list1.append(2020)
print ("New List: ", list1)

#Insert
list1.insert(0, 'Python')
print("After inserting: ", list1)

#del 
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

#pop 
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop()
print ("The first motorcycle I owned was a ", first_owned)

#remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

