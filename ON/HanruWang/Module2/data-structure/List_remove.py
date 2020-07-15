moto = ['honda', 'yamaha', 'suzuki']
# del moto[1]
# print(moto)

popped_moto = moto.pop()
print(moto)
print(popped_moto)

first_owned = moto.pop(0)
print("My first moto was a", first_owned)

moto = ['honda', 'yamaha', 'suzuki', 'ducati']
moto.remove('ducati')
print(moto)
