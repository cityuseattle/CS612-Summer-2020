motorcycles = ['honda','yamaha','suzuki']
popped_motorcycle = motorcycles.pop()
del motorcycles[1]
print(motorcycles)

print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("the first motorcycle I owned was a ",first_owned)

motorcycles = ['honda','yamaha','suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)