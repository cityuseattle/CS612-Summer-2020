moto = ['honda', 'yamaha', 'suzuki', 'ducati']
popped_moto = moto.pop()
del moto[1]
print(moto)
print(popped_moto)
first_owned = moto.pop(0)

print ("The first moto I owned was a ", first_owned)

moto.remove('ducati')
print(moto)