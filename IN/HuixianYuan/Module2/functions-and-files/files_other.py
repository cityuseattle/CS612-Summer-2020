with open('hello.txt') as file_objct:
    contents = file_objct.read()

print(contents)
print(contents.rstrip())