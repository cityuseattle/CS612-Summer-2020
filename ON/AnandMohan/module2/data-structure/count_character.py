import pprint

message="""Peter piper picked a peck of pickled peppers
            A peck of pickled peppers peter piper picked
            if peter piper picked a peck of pickled peppers
            where's the peck of pickled peppers peter piper picked?"""

count={}
for char in message:
    count.setdefault(char,0)
    count[char]=count[char]+1

pprint.pprint(count)