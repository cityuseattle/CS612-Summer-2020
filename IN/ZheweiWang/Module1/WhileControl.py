print(' This prog will sum from 1 to a number you enterd')
print("please enter a number")
num=int(input())
total=0

while num>=1:
    total +=num
    num -=1

print("the sum is "+ str(total))