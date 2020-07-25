# Yuhan Guo
# 07/24/2020

file = open('hello.txt','a')
file.write('\nThis is new content I just appended')
file.close()

new_file = open('word.txt', 'w')
new_file.write('This is new file')
new_file.close()

file = open('hello.txt')
content = file.read()
file.close()
print(content)