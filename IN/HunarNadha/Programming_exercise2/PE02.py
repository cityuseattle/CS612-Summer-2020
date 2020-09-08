# Function to check if given three points form a triangle  
def isTriangle(x,y):       
    # Condition to check if area is not equal to 0  
    if areaOfTriangle(x,y) == 0: 
        return False
    else: 
        return True
     
# Area of triangle     
def areaOfTriangle(x,y):
    area = (abs(x[0]*y[1] + x[1]*y[2] + x[2]*y[0] - x[0]*y[2] - x[1]*y[0] - x[2]*y[1]))/2
    return area

# Perimeter of triangle     
def perimeterOfTriangle(x,y):
    return(distance(x[0],y[0],x[1],y[1])+distance(x[0],y[0],x[2],y[2])+distance(x[1],y[1],x[2],y[2]))

# Calculate distance between x1 and x2, y1 and y2
def distance(x1,y1,x2,y2):
    return((x1-x2)**2 + (y1-y2)**2)**0.5    
     
# Main call
if __name__ == "__main__":
    x=[]
    y=[]
    Input_file = open('Inputfile.txt','r').readlines()
    isFirstLine = True
    for line in Input_file:
        if isFirstLine:
            checkForPerimeter = Input_file[0]
        else:        
            row = line.strip().split(',')
            x.append(float(row[0].strip()))
            y.append(float(row[1].strip()))

        isFirstLine = False
        
    if isTriangle(x,y) == False:
        raise Exception("Error: This is not a triangle") 
    else: 
        print('The given coordinates does form a triangle')

    if checkForPerimeter.strip() == "False":
        print('Since the given boolean variable is False, hence calculating area.')
        area = areaOfTriangle(x,y)
        print('Area of triangle is : ', area)
    else:
        print('Since the given boolean variable is True, hence calculating perimeter')
        permimeter = perimeterOfTriangle(x,y)
        print('Perimeter of triangle is : ', permimeter)
   

          