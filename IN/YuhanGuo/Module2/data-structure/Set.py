# Yuhan Guo
# 07/23/2020

#joining two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)

print("Set3:\n", set3)
set1.update(set2)
print("Updated Set1:\n", set1)

#constructor
thisset = set(("apple", "banana", "cherry"))
print("Constructor made set:\n", thisset)