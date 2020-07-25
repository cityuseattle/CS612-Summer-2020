# Yuhan Guo
# 07/24/2020

try:
    fh = open("tetsfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
