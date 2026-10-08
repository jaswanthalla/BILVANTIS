# Write a Python program to find the second largest number in a list without using sort() or sorted(). 

# Input: [10, 20, 4, 45, 99] 

# Output: 45 

list = [1, 2, 3, 4, 5]

largest = list[0]
for i in list:
    if i > largest:
        largest = i
second = list[0]
for i in list:
    if i != largest and i > second:
        second = i
print(second)
