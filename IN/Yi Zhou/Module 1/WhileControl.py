print('This program will sum of number from 1 to a number you enter.')
print('Please enter  a ending number: ')
num=int(input())

total=0

while num>=1:
    total+=num
    num-=1

print('This sum is :'+ str(total))