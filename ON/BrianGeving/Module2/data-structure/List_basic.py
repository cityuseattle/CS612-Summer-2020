list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
#accessing
print("list1[0]: ",list1[0])
print("list2[1:5]: ",list2[1:5])
print("Value available at index 2 : ")
print(list1[2])
#updating
list1[2] = 2001
print("New value available at index 2 : ")
print(list1[2])
#adding
list1.append(2020)
print("New list: ",list1)
#insert
list1.insert(0, 'Python')
print("After inserting: ", list1)