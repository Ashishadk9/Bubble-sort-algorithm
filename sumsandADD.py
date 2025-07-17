#Q4
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
print(list1)
print(list2)
result = []
for i in range(len(list2)):  # Since both lists have 6 elements
    result.append(list1[i])
    result.append(list2[i])

print(result)