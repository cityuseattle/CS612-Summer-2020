try:
    fh = open("testfile", "r") #this file I don't have written ('w') permissions
    fh.write("This is my test file for exception handling!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
