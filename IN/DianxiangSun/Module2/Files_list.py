filename = 'hello.txt'

with open(filename) as file_object:
     lines = file_object.readline()

for line in lines:
    print(line.rstrip())