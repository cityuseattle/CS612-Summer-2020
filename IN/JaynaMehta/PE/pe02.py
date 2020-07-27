def area_of_triangle(x,y,z):

  area = abs(float(x[0])*float(y[1]) + float(y[0])*float(z[1]) + float(z[0])*float(x[1]) 
        - float(x[0])*float(z[1]) - float(y[0])*float(x[1]) - float(z[0])*float(y[1]))/ 2

  if area > 0:

    return area

  else:

    return "Error. Given co-ordinates don't form a triangle"

def perimeter_of_triangle(x,y,z):

  a = ((float(x[0])-float(y[0]))**2 + (float(y[1])-float(x[1]))**2)**0.5

  b = ((float(y[0])-float(z[0]))**2 + (float(y[1])-float(z[1]))**2)**0.5

  c = ((float(x[0])-float(z[0]))**2 + (float(x[1])-float(z[1]))**2)**0.5
  perimeter = a + b + c

  if (a + b > c) and (a + c > b) and (b + c > a):

    return perimeter

  else:

    return "Error. Given co-ordinates don't form a triangle"

def main():

  f = open("input_pe02.txt","r")

  boolean_value = f.readline()

  x = (f.readline()).split(',')

  y = (f.readline()).split(',')

  z = (f.readline()).split(',')

  if boolean_value.lower() == "false\n":

    print("Area of triangle: ",area_of_triangle(x,y,z))

  else:

    print("Perimeter of triangle: ",perimeter_of_triangle(x,y,z))

main()