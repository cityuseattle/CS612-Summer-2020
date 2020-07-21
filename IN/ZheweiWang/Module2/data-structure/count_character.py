import pprint

message= """Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
Where's the peck of pickled peppers Peter Piper picked?"""

count= {}
for charac in message:
    count.setdefault(charac, 0)
    count[charac]=count[charac]+1

pprint.pprint(count)