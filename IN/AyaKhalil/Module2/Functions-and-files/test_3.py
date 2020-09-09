try:
    fh=open("testfile","w")
    try:
        fh.write("ths is a test for exception handling")
        raise IOError
    finally:
        print("going to close the file")
except IOError:
    print("Error:can\'t find file or read data")