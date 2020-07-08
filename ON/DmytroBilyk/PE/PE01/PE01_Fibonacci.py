# initialize variables
topNumber = 100
numberOne = 0
numberTwo = 1
counter = 1

# display numbers
print(str(counter) + ": Value is: " + str(numberOne))

counter += 1
print(str(counter) + ": Value is: " + str(numberTwo))

# display first 100 fibonacci numbers
while counter < topNumber:
    # update the counter
    counter += 1

    # find the next number
    fibonacci = numberOne + numberTwo

    # dispaly list that contains Fibonacci numbers
    print(str(counter) + ". Value is: " + str(fibonacci))

    # update number one and number two
    numberOne = numberTwo
    numberTwo = fibonacci
