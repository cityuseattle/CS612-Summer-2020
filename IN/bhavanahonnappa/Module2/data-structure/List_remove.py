#del
motorcycles = ['honda' , 'Yahama', 'suzuki']
del motorcycles[1]
print(motorcycles)

#pop
motorcycles = ['honda' , 'Yahama', 'suzuki']
popped_motorcycles =  motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
first_owned= motorcycles.pop(0)
print("the motorcycle that i owned was a", first_owned)

#remove
motorcycles = ['honda' , 'Yahama', 'suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)
