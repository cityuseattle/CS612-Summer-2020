import pprint
message= """Peter piper picked a peck of pickled peppers 
            A peck of pickled peppers Peter piper picked
            if Peter piper picked a peck of pickled peppers 
            where is the peck of pickled peppers Peter piper picked?"""


count= {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)