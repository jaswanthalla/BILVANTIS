n = int(input("enter the number of elements in the list:"))
list = []

for i in range(n):
    num = int(input("enter a number:"))
    list.append(num)

print(list)
largest1 = max(list)
print(largest1)

largest2 = list[0]
for a in list:
    if a > largest2:
        largest2 = a
print(largest2)