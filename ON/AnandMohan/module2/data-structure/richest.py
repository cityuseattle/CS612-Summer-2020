income={'Alice':9000,
        'Bob':10000,
        'Jeff':20000,
        'Apiwat':99998,
        'Stark':999999}

highest=max(income,key=income.get)
print("Rich man:",end='')
print(highest+' with $'+str(income[highest]))