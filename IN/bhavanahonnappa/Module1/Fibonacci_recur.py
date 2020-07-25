from functools import lru_cache
@lru_cache

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        return fibonacci(i-1)**0.5 + fibonacci(i-2)**1.1

num = int(input("Enter a integer between 0 to 105: "))

if num <= 0:
    print ("Please enter a positive number")
elif num > 105:
    print ("Number is greater than 105")
else:
    for i in range (num):
        print(i, ":", fibonacci(i))
    