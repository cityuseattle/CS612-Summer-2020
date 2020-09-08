aliens_0 = {'color': 'green', 'points' : 5}
aliens_1 = {'color' : 'yellow' , 'points' : 10}

aliens = [aliens_0, aliens_1]

for i in aliens:
    for key,value in i.items():
        print("KEY: ", key, "\t", "VALUE:", value)
        