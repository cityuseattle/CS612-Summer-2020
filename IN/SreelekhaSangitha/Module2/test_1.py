try:
    fh = open("testfile", "w")
    fh.write("This is my test exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file succesully")
fh.close()
