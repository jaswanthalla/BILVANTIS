s = {1, 2, 3, 3, 2}
print(s)  # duplicates removed
s.add(4)
s.update([5, 6])
s.remove(6)  # error if missing
s.discard(99)  # no error if missing
print(s)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B, A.union(B))
print(A & B, A.intersection(B))
print(A - B, A.difference(B))
print(A ^ B)
print({1, 2} <= A, A.isdisjoint({9}))
print(list(set([1, 1, 2, 3, 3])))  # remove duplicates from list
print(type({}), type(set()))
