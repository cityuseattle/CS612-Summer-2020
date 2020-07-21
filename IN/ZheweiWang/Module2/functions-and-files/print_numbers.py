def numbers(limit):
    i=0
    numbers=[]

    while i < limit:
        numbers.append(i)
        i=i+1
    return numbers

usr_limit= int(input("Give a limit: "))
print(numbers(usr_limit))