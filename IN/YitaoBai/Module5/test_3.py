try:
    fh = open("testfile",'w')
    try:
        fh.write("this is my test file for exception handling")
        raise IOError
    finally:
        print("going to close file")
except IOError:
    print("error can\'t find file or read data")
