try:
    fh = open("testfile", 'w')
    fh.write("This is my test file for exception handling !!")
except IOError:
    print("Error: can\'t find or reach data")
else:
    print("Written contents in the file successfully")
    fh.close()