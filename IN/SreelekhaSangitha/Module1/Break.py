print("For-Break")
for letter in 'python':
    if letter == 'h':
        break
    print ( 'Current Letter : ' ,letter)
print("\nWhile-Break")
var=10
while var > 0:
    print("Current vaiable value :", var)
    var= var-1
    if var == 5:
        break
print("Good Bye!")
