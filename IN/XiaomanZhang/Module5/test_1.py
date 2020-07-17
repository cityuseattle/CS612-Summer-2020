try:
    fh = open("testfile","w")
    fh.write("this is my test file for exception handling")
except I0Error:
    print("error: can\'t find file or read data")
else:
    print("written content in the file successfully")
    fh.close()