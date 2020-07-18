list1 = ['physics', 'chemistry', 1997, 2000]; 
list2 = [1, 2, 3, 4, 5 ]; 

# accessing
print("list1[0]", list1[0] )
print("list2[1:5", list2[1:5])
# updating
print("Value available at index 2:")
print(list1[2])
list1[2] = 2001
print("New value available at index 2:")
print(list1[2])
#adding
list1.append(2020)
print("New list", list1)
#insert
list1.insert(0,"Python")
print("After inserting: ", list1)
#del
motorcycles = ["honda","yamaha","suzuki"]
del motorcycles[1]
print (motorcycles)
#pop
motorcycles = ["honda","yamaha","suzuki"]
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
fisrt_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a", fisrt_owned)
#remove 
motorcycles = ["honda","yamaha","suzuki","ducati"]
motorcycles.remove("ducati")
print(motorcycles)
