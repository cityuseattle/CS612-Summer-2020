
with open('input_pe02.txt') as f:
    lines = [x.rstrip() for x in f]

p1 = lines[1]
x1 = float(p1[:1])
y1 = float(p1[2:])

p2 = lines[2]
x2 = float(p2[:1])
y2 = float(p2[2:])

p3 = lines[3]
x3 = float(p3[:1])
y3 = float(p3[2:])

if lines[0] == 'True':
    perimeter = ((x1 - x2)**2 + (y1 - y2)**2)**0.5 + ((x1 - x3)**2 + (y1 - y3)**2)**0.5 + ((x3 - x2)**2 + (y3 - y2)**2)**0.5
    print('Perimeter of the triangle: ',"%.3f" %perimeter)
else:
    area = abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)/2
    print('Area of the triangle: ', area)



