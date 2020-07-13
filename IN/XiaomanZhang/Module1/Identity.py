a = 20 
b = 20

if (a is b) :
    print("line 1- a and b have the same identity")
else:
    print("line1- a and b donot have the same identity")

if (id(a) == id(b)):
    print("line2- a and b have the same identity")
else:
    print("line2- a and b donot have the same identity")

b = 30
if (a is b) :
    print("line3- a and b have the same identity")
else:
    print("line3- a and b donot have the same identity")

if (a is not b) :
    print("line4- a and b donot have the same identity")
else:
    print("line4- a and b have the same identity")