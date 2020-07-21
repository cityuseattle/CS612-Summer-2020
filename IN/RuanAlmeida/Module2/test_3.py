try:
    fh = open("testfile", "w")
    try:
        fh.write("this is my test file for exception handling!!")
        raise IOError
    finally:
        print("going to close the file")
except IOError:
    print("error: cant find file or read data")
