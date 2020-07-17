try:
    fh = open("testfile","w")
    try:
        fh.write("this is my test file for exception handling!!!")
        raise IOError
    finally:
        print("going to close the file")
except IOError:
    print("Error: cann't find file or read data")