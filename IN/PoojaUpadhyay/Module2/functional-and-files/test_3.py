try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling") 
        raise IOError
    finally:
        print("Going to close the file ")
except IOError:
    print("Error: cann't find or read data")

x = ['P', 'y', 't', 'h', 'o', 'n'] 
for i in enumerate(x):  
    print(i,end= "") 
    
x = {5:4, 8:8, 3:16, 9:32} tp
print(sorted(x.items())) 

x = [5, 4, 3, 2] 
x.insert(1,0) 
print(x) 