import math

def fib(n):
    a = 0.0
    print(a)
    b = 1.0
    print(b)
    for i in range(2,n):
        c = math.pow(a,1.1) + math.pow(b,0.5)
        a = b
        b = c
        print(c)
fib(100)
