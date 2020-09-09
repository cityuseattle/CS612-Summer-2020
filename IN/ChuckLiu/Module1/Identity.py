a = 20
b = 20

if (a is b):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")

if (id(a) == id(b)):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")

b = 30
if (a is b):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")

if (a is not b):
    print ("a and b do not have same identity")
else:
    print ("a and b have same identity")