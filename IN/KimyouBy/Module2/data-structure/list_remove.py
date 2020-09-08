#deleting
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
del motorcycles[1]
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a", first_owned)

#remove
motorcycles.remove('ducati')
print(motorcycles)