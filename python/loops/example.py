for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
for ch in "Hi":
    print(ch, end=" ")
print()
for i, v in enumerate(["a", "b", "c"], start=1):
    print(i, v)
for n, s in zip([1, 2, 3], ["one", "two", "three"]):
    print(n, s)
# nested loop - right triangle pattern
for i in range(1, 5):
    print("*" * i)
# for...else
for n in range(2, 5):
    if n == 10:
        break
else:
    print("loop completed without break")
