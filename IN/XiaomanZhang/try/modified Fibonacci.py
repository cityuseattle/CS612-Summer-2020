
def MF( n ):
    a1 = 0
    a2 = 1
    print(1 ,a1)
    print(2, a2)
    for i in range(3, n+1):
        a3 = a2 ** 0.5 + a1 ** 1.1
        a1 = a2
        a2 = a3
        print(i , round(a3,2))
                    

print(MF(100))