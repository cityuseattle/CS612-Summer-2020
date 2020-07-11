print(f'for-continue')
for letter in 'Python':
    if letter == 'h':
        continue
    print('current letter :', letter)

print("\n while-continue")
var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print ('current variable value:', var)
print ("good bye!")