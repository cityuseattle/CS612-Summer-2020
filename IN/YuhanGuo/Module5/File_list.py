# Yuhan Guo
# 07/24/2020

filename = 'hello.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
