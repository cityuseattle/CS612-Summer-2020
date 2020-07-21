
f = open("input_pe02.txt", 'r')
Perimeter = f.readline().strip()
cord1 = "[" + f.readline().strip() + "]"
cord2 = "[" + f.readline().strip() + "]"
cord3 = "[" + f.readline().strip() + "]"

# converting string to list
cord1 = cord1.strip('][').split(', ') 
cord2 = cord2.strip('][').split(', ') 
cord3 = cord3.strip('][').split(', ') 

side1 = ((float(cord1[0])-float(cord2[0]))**2 + (float(cord1[1])-float(cord2[1]))**2)**0.5
side2 = ((float(cord1[0])-float(cord3[0]))**2 + (float(cord1[1])-float(cord3[1]))**2)**0.5
side3 = ((float(cord2[0])-float(cord3[0]))**2 + (float(cord2[1])-float(cord3[1]))**2)**0.5

def CheckTriangle():
    if side1<=0 or side2<=0 or side3<=0:
        print("ERROR: the coordinates does not form a triangle!")
        return False
    else:    
        return True


def CalcPerimeter():
    if CheckTriangle():
        return side1 + side2 + side3
    else: 
        return 0     

def CalcArea():
    Area = (float(cord1[0])*float(cord2[1]) + float(cord2[0])*float(cord3[1]) + float(cord3[0])*float(cord1[1]) - 
      float(cord1[0])*float(cord3[1]) - float(cord2[0])*float(cord1[1]) - float(cord3[0])*float(cord2[1])) / 2
    Area = abs(Area)  
    return Area

# driver code
print("Cordinates: ")
print(cord1)
print(cord2)
print(cord3)

if CheckTriangle():
    if (Perimeter == "True"):
        print("Perimeter of the triangle: ")  
        print(CalcPerimeter())
    else:
        print("Area of the triangle: ")  
        print(CalcArea())
