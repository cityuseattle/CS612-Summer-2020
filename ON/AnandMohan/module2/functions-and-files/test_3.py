try:
    fh=open("//Users//eer6//cityu//CS612-Summer-2020//ON//AnandMohan//module2//testfile","w")
    try:
        fh.write("This is my test file for exception handling!!")
        raise IOError
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can't find the file")
