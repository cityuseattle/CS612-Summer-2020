a = 20
b = 20

if (a is b):
    print("line 1 - a and b have same id")
else:
    print("line 1 - a and b do not have same id") 

if ( id(a) == id(b)):
    print("line 2 - a and b have same id")
else:
    print("line 2 - a and b do not have same id") 

b = 30
if (a is b):
    print("line 3 - a and b have same id")
else:
    print("line 3 - a and b do not have same id") 

if (a is not b):
    print("line 4 - a and b do not have same id")
else:
    print("line 4 - a and b have same id") 