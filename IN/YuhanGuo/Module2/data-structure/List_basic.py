# Yuhan Guo
# 07/16/2020

list1 = ['physics', 'chemistry', 1997,2000]
list2 = range(1,8)

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

print("Value at list1 index 2: ")
print(list1[2])
list1[2] = 2001
print("New Value at list1 index 2: ")
print(list1[2])

list1.append(2020)
print("New List:", list1)

list1.insert(0, 'Python')
print("After inserting: ", list1)