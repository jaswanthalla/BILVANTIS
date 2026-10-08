# Write a Python program using lambda with filter() and map() to get all words longer than 4 characters from a list and convert them to upper case.

# Original list: ['sun', 'python', 'code', 'java', 'program']

# Output: ['PYTHON', 'PROGRAM']

items = int(input("enter no of items in the list:"))

list1 = []

for i in range(items):
    item = str(input("Enter the strings to the list:"))
    list1.append(item)


output = filter(lambda x: len(x) > 4, list1)

final = list(map(lambda y: y.upper(), output))
print(final)
