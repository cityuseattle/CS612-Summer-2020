motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle=motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
first_owned = motorcycles.pop()
print("first motorcycle I owned was a ", first_owned)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)