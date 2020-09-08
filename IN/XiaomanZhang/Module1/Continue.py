print("for - continue")
for letter in "Python":
    if letter == 'h':
        continue
    print("current letter is ", letter)

print("while- continue")
var = 10
while var >0:
    var = var -1
    if var ==5:
        continue
    print("current variable value is: ", var)
print("good bye")