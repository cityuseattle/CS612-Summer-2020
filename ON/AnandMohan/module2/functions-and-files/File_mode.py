file= open('/Users/eer6/cityu/CS612-Summer-2020/ON/AnandMohan/module2/hello.txt','a')
file.write('\nThis is new content I just appended')
file.close

new_file=open('/Users/eer6/cityu/CS612-Summer-2020/ON/AnandMohan/module2/world.txt','w')
new_file.write('This is new file')
new_file.close

file=open('/Users/eer6/cityu/CS612-Summer-2020/ON/AnandMohan/module2/hello.txt')
content=file.read()
file.close()
print(content)