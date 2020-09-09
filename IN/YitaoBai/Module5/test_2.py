try:
    fh = open("testfile",'r')
    fh.write("this is my test file for exception handling")
except IOError:
    print("error can\'t find file or read data")
else:
    print("written content in the file successsfully")
    fh.close()