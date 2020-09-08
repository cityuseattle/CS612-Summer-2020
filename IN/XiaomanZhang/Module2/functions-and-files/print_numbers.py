def numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        numbers.append(i)
        i = i +1
    return numbers

user_limit = int(input("giva a limit:"))
print(numbers(user_limit))