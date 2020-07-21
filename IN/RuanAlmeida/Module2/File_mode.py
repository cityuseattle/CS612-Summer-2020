file = open ('hello.txt', 'a') 
file.write('\nThis is a new content i just appended')
file.close

new_file = open('world.txt', 'w')
new_file.write('this is a new file')
new_file.close()

file = open('hello.txt')
content = file.read()
file.close()
print(content)