t = (10, 20, 30, 20)
print(t[0], t[-1], t[1:3], t.count(20), t.index(30))
single = (5,)  # comma is required
print(type(single), type((5)))
a, b, c, d = t  # unpacking
print(a, d)
first, *rest = t  # extended unpacking
print(first, rest)
try:
    t[0] = 99
except TypeError as e:
    print("Error:", e)
lst = list(t)
lst.append(40)
t = tuple(lst)  # "modify" by converting
print(t)
