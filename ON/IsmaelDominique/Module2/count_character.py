import pprint

message = """Peter Piper picked a peck of picked if peter piper picked a peck of pickled peppers where's the peck of pickled peppers piper picked"""

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

    pprint.pprint(count)
    