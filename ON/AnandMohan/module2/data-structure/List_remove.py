# del
motorcycles=['honda','yamaha','suzuki']
del motorcycles[1]
print(motorcycles)
# pop
motorcycles=['honda','yamaha','suzuki']
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned=motorcycles.pop(0)
print("The first motorcycle 1 owned as a ",first_owned)
# Remove
motorcycles=['honda','yamaha','suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)