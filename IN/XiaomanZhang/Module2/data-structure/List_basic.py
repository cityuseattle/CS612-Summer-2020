list1 = ['physics', 'chemestry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]", list1[0])
print("list2[1:5]", list2[1:5])
#updating
print("value available at index 2: ")
print(list1[2])
list1[2] = 2001
print("new value available at index 2: ")
print(list1[2])
#adding
list1.append(2020)
print("new list1: ", list1)
#inserting
list1.insert(1, 'Python')
print("after inserting: ", list1)

