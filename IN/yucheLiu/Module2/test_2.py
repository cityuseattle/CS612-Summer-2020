try:
    fh = open("testfile","r")
    fh.write("this is the new file for error handling")
except IOError:
    print("ERROR: can't find the data")
else:
    print("Successfully")
    fh.close()