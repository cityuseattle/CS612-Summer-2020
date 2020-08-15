f = open('input_pe02.txt', "r")
lines = f.readlines()
fields = lines[1].split(",")
x1 = float(fields[0]) 
y1 = float(fields[1])
fields = lines[2].split(",")
x2 = float(fields[0]) 
y2 = float(fields[1])
fields = lines[3].split(",")
x3 = float(fields[0]) 
y3 = float(fields[1])
perimeter = float((((x1-x2)**2 + (y1-y2)**2)**0.5) + (((x2-x3)**2 + (y2-y3)**2)**0.5) + (((x3-x1)**2 + (y3-y1)**2)**0.5))
area = float(abs((x1*y2) + (x2*y3) + (x3*y1) - (x1*y3) - (x2*y1) - (x3*y2)) / 2)
if lines[0]=="True":
    if perimeter<=0:
        print("Not forming a Triangle")
    else :
        print(perimeter)
else :
    if area<=0:
        print("Not forming a Triangle")
    else :
        print(area)
f.close()