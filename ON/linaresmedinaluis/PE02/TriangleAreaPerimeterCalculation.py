							
def CalculateOperation(Coordinates):

    #Calculate the distance of each side of the triangle A, B, C  
    A = GetDistance( Coordinates[1],  Coordinates[2])    
    B = GetDistance( Coordinates[2],  Coordinates[3])    
    C = GetDistance( Coordinates[1],  Coordinates[3])    
    print(f'Triangle coordinates: {Coordinates[1]},{Coordinates[2]},{Coordinates[3]}\n')

    #Evaluate calculation
    Calculation = Coordinates[0]
    
    #Evaluate operation to calculate
    if Calculation == 'Perimeter':

        #Calculate triangle perimeter for A,B,C 
        print(f'Perimeter of the triangle is: {GetTrianglePerimeter(A, B, C)}\n')

    elif Calculation == "Area":
        
        #Calculate triangle area for A,B,C 
        print(f'Area of the triangle is: {GetTriangleArea(A, B, C)}\n')

    else:

        print(f'invalid calculation ( True:Perimeter, False:Area )\n')
    return


def GetDistance(Coordinate1, Coordinate2):
    #Math library is required 
    import math

    #Euclidian distance calculation for sitance between 2 coordinates
    Distance = math.sqrt( ((Coordinate1[0]-Coordinate2[0])**2)+((Coordinate1[1]-Coordinate2[1])**2) )

    return float(Distance)

def GetTriangleArea(A, B, C):
    #Calculate the triangle sides
    Sides = (A + B + C) / 2

    #Calculate the area 
    Area = (Sides*(Sides-A)*(Sides-B)*(Sides-C)) ** 0.5
    
    return float(Area)

def GetTrianglePerimeter(A, B, C):

    # Calculate the perimeter
    Perimeter = A + B + C

    return float(Perimeter)

def ReadConfiguration():
    #Initiate the operation and coordinates list 
    Configuration = []

    #Read file with coordinates and configuration for calculation
    with open('input_pe02.txt') as File:

        for Line in File:
            #Evaluate line for perimeter
            if Line == 'True\n':
                Configuration.append('Perimeter')

            #Evaluate line for area    
            elif Line == 'False\n':
                Configuration.append('Area')

            #Evaluate line for coordinates
            else:
                #Spit the coordinates in X and Y 
                X, Y = Line.split(', ')
                
                #Create the tuple for each coordinate
                Vertex =(float(X), float(Y))
                
                #Add the tuple to the coordinate list
                Configuration.append(Vertex)

    return Configuration

#main program

#Read configuration with Calculation(Perimeter/Area) and triangle coordinates 
Configuration = ReadConfiguration()

#Calculate operation
CalculateOperation(Configuration)

print(f'Good bye!\n\n') 


