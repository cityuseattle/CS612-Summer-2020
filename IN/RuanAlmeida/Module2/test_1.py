try:
    fh = open("testfile", "w")
    fh.write("this is my test file for exception handling!!")
except IOError:
    print("error: cant find file or read data")
else:
    print("written content in the file sucessfully")
    fh.close()