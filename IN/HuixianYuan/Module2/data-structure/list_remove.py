#del
motorcycles = ['honda',  'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

#pop
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motrocycle = motorcycles.pop()
print(motorcycles)
print(popped_motrocycle)
first_owned = motorcycles.pop(0)
print("the first motorcycle I owned was a", first_owned)

# remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
