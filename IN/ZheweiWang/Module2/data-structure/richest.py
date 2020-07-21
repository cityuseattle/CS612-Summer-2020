income={'alice':90000,
'bob':100000,
'jeff':200000,
'Apiwat':999998,
'stark':999999}

highest=max(income,key=income.get)
print("the richest man on earth", end=' ')
print(highest+'with $'+str(income[highest]))