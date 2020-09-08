print('This program will sum no. from 1 to number you enter')
print("please enter a number:")
num = int(input())
total = 0

while num>= 1:
    total += num
    num -= 1
print('The sum is :'+str(total))

