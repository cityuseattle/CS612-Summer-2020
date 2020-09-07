import pprint

message = """Peter piper picked a peck of picled peppers 
            A peck of pickled peppers peter piper picked
            If peter piper picked a peck of pickled peppers
            where's the peck of pickled peppers peter piper picked?"""

count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)
