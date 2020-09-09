print('for-continue')
for letter in 'python':
    if letter == 'h':
        continue
    print('current letter : ', letter)

print('\nwhile-continue')
var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('current variable value : ', var)
print('good bye!')