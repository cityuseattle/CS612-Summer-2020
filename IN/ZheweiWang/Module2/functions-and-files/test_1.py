try:
    fh=open("testfile","w")
    fh.write("ths is a test for exception handling")
except IOError:
    print("Error:can\'t find file or read data")
else:
    print("written content in the file successfully")
    fh.close()