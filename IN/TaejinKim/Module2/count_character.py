import pprint

message = """Peter Piper pocked a peck of pickled peppers
            a peck of pickled peppers Peter Piper picked 
            If Peter Piper picked a peck of pickled peppers
            where's the peck of pickled peppers Peter piper picked?"""
count ={}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] +1
            
pprint.pprint(count)