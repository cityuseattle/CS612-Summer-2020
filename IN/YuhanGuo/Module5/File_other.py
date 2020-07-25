# Yuhan Guo
# 07/24/2020

with open('hello.txt') as file_object: # with ensures safe file open/close
    contents = file_object.read()
print(contents)