# Q3
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
print(l1)
print(l2)
combined = []
for i in range(len(l2)):
    combined.append(l1[i])
    combined.append(l2[i])
print(combined)