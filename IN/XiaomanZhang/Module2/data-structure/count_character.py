import pprint

message = """ peter piper picked a peck of pickled pepers 
                a peck of pickled pepers Peter Piper picked
                if Peter Piper picked a peck of pickled pepper
                where is the peck of pickled peper Peter Piper picked?"""

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)