try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
        raise IOError
    finally:
        print("Going to closethe file")
except IOError:
    print("Error: can\'t find file or read data")

