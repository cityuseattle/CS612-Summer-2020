orginal= [8,20,-10,0,55,-777]

for i in range(len(orginal)):
    if orginal[i]<0:
        orginal[i]=abs(orginal[i])
print(orginal)