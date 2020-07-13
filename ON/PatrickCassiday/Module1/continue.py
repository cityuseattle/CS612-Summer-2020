print("For-Break")
for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :', letter)

print("\nWhile-Break")
var = 10
while var >= 0: #Had to change to >= from > to get the result to 0
    print('Current variable value :', var)
    var = var - 1
    if var ==5:
        continue
print("Good bye!")
