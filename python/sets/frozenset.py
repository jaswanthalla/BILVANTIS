fs = frozenset([1, 2, 3, 3])
print(fs, type(fs))
print(fs | frozenset([4]))  # operations return new frozensets
print(fs & {2, 3, 9})
try:
    fs.add(5)
except AttributeError as e:
    print("Error:", e)
d = {frozenset([1, 2]): "pair"}  # usable as dict key
print(d[frozenset([2, 1])])
nested = {frozenset([1]), frozenset([2])}
print(len(nested))
