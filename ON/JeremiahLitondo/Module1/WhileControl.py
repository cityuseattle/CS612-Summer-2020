print("Tis program will sum of numbers from 1 to a number that you enter.")

print("please enter an ending number: ")
num = int(input())

total = 0

while num >=1:
    total += num
    num -= 1

print("The sum is: " + str(total))
