import pprint

message = """Peter Piper picked a peck of pickled peppers 
            im not typing this..."""
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)