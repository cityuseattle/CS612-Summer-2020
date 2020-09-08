import pprint
message = "hello everyone"

count={}

for cha in message:
    count.setdefault(cha,0)
    count[cha] = count[cha]+1

pprint.pprint(count)