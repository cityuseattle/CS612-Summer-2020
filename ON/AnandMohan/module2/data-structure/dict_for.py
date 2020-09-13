alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}

aliens=[alien_0,alien_1]

# Accessing key,value
for i in aliens:
    for k,v in i.items():
        print("KEY:",k,"\t", "VALUE:",v)