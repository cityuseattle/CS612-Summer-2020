try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling")
        raise IOError
    finally:
        print("Error: can\'t find file or read data")
        fh.close()
except IOError:
    print("Written content in the file succesfully")
    

