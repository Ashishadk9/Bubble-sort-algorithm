# Q2
# Input list
original_list=[43,23,21,44,56,75]
# List to store elements of even position
even_position_list=[]
# Using loop in original list
for i in range(len(original_list)):
    if i % 2==1:
        even_position_list.append(original_list[i])# add the elements
        
    print(even_position_list)