a = 20
b = 20

if ( a is b):
	print("Line 1 - a and b have same identify")
else:
	print("Line 1 - a and b do not have same identify")
	
if ( id(a) == id(b) ):
	print("Line 2 - a and b have same identify")
else:
	print("Line 2 - a and b do not have same identify")
	
b = 30
if (a is b):
	print("Line 3 -a and b have same identify")
else:
	print ("Line 3 -a and b do not have same identify")
	
if (a is not b):
	print ("Line 4 - a and b do not have same identify")
else:
	print("Line 4 - a and b have same identify ")
								