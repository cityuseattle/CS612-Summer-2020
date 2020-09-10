# Function for nth Fibonacci number 
  
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
         return Fibonacci(n-1)+Fibonacci(n-2) 
       # return Fibonacci(pow(n-1, 0.5))+Fibonacci(pow(n-2, 1.1)) 
  
# Driver Program 

Fib_num = 1
total_Fib = int(input("Enter the number of items you want on your fibonacci list: "))
while total_Fib > 0:
    print(str(Fibonacci(Fib_num))) 
    Fib_num = Fib_num + 1
    total_Fib = total_Fib - 1
 