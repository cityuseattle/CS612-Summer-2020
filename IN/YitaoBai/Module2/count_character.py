import pprint
message = """The output would look like this with pprint().
            While the print() will show result in horizontal format which 
            is difficult to read. The count = 
            is the empty dictionary. """

count={}
for character in message:
     count.setdefault(character,0)
     count[character] = count[character] + 1

pprint.pprint(count)