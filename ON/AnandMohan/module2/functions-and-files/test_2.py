try:
    fh=open("//Users//eer6//cityu//CS612-Summer-2020//ON//AnandMohan//module2//testfile","r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can't find the file")
else:
    print("Written content in the file successfully")
fh.close()