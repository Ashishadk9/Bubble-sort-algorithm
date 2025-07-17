# Q1
# Input list
a=[2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]

# Print the elements are divisible by 2 and 3.
for n in a:
    if n % 2==0 and n % 3==0:
        print(n)