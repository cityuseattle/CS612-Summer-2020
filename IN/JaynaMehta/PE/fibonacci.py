import math
n = int(input("Enter Fibonacci numbers "))

a, b = 0, 1
count = 0

if n<= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(a) 
else:
   print("Fibonacci sequence:")
   while count < n:
       print(a)
       c =math.pow(b,0.5) + math.pow(a,1.1)
       a = b
       b = c
       count += 1