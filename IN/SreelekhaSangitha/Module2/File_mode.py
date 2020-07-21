file = open('Module2/hello.txt', 'a')
file.write('\nThis is new content I just appended')
file.close()

new_file = open('Module2/world.txt', 'w')
new_file.write('This is new file')
new_file.close()

file = open('Module2/hello.txt')
content = file.read()
file.close()
print(content)
