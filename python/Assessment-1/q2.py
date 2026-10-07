# 2. Write a Python program to find how many times each number appears in a list using loops.

# numbers = [2, 4, 2, 5, 4, 2, 7, 5]


numbers = [2, 4, 2, 5, 4, 2, 7, 5]

dict = {}

for num in numbers:
    if num in dict:
        dict[num] = dict[num] + 1
    else:
        dict[num] = 1

print(dict)

for k, v in dict.items():
    print(f"{k} repeats {v} times")
