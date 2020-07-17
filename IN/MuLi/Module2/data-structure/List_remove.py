#del
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]
print(motorcycles)
#pop
motorcycles = ['honda','yamaha','suzuki']
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a", first_owned)
#remove
motorcycle = ['honda','yamaha','suzuki','ducati']
motorcycle.remove('ducati')
print(motorcycle)