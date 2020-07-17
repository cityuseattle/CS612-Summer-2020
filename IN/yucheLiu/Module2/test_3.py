try:
    fh = open("testfile","w")
    try:
        fh.write("this is the new file for error handling")
        raise IOError
    finally:
        print("going to close the file")
except IOError:
    print("ERROR: can't find the data")