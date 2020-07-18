alien_0 = {'color': 'green','points':5}
alien_1 = {'color': 'yellow', 'points':10}

aliens = [alien_0,alien_1]

#accessin key values
for i in aliens:
    for key, value in i.items():
        print("KEY: ", key, "\t", "VALUE :", value)