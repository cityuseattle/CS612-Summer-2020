print("This program will sum of the numbers form 1 to another number you enter")
print('Please enter an ending number:')
num=int(input())

total=0
while num>=1:
    total+=num
    num-=1
print('The sume is : '+str(total))