income = {'alice':90000,
'bob':100000,
'jeff':20000,
'apiwat':999998,
'stark':999999}

highest = max(income,key=income.get)
print("the riches man on earth :",end=' ')
print(highest + ' with $'+str(income[highest]))