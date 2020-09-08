motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first motorcysle I owned was a", first_owned)

motorcycles =  ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)