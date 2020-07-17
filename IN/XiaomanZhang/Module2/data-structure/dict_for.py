alien0 = {'color':'green', 'points':5}
alien1 = {'color': 'yellow', 'points':10}

aliens = [alien0, alien1]

#accessing key, value
for i in aliens:
    for key,value in i.items():
        print("KEY:", key,"\t", "VALUE:", value)