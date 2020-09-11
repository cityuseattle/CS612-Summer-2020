filename = 'hello.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for lines in lines:
    print(lines.rstrip())

