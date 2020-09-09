# Joining two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

#constructor
thisSet = set(("Apple", "Banana", "Cherry"))
print(thisSet)
print(type(thisSet))