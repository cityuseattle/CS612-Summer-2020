print("For-Continue")
for letter in 'python':
    if letter == 'h':
        continue
    print ( 'Current Letter : ' ,letter)
print("\nWhile-Continue")
var=10
while var > 0:
    print("Current vaiable value :", var)
    var= var-1
    if var == 5:
        continue
print("Good Bye!")