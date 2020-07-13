print('How old are you?')
age = int(input())
#believe that the age should be below 21 for the proper check on age
if age < 21:
    print('you are too young to have a drink.')
elif age >= 80:
    print('Ok, you will get a free drink.')
else:
    print('Sure, enjoy your drink')