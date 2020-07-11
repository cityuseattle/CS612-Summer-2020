print("for -break")
for letter in 'Python':
    if letter == 'h':
        break
    print("current letter : ",letter)

print("\nWhile-break")
var = 10
while var > 0:
    print("current variable value : ",var)
    var = var - 1
    if var == 5:
        break
print("goodbye")