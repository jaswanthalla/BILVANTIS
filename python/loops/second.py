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
