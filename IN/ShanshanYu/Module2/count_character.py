import pprint

message = """Peter Piper picked a peck of pickled pepers
             A peck of pickled pepers Peter Piper picked
             If Peter Piper picked a peck of pickled pepers
             Where's the peck of picled pepers Peter Piper picked?"""

count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)