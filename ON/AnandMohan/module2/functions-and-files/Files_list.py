filename='/Users/eer6/cityu/CS612-Summer-2020/ON/AnandMohan/module2/hello.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())