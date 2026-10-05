student = {"name": "Asha", "age": 20, "course": "CS"}
print(student["name"], student.get("grade", "N/A"))
student["age"] = 21  # update
student["city"] = "Hyderabad"  # add
del student["course"]  # delete
print(student)
for k, v in student.items():
    print(k, "->", v)
print(list(student.keys()), list(student.values()))
print("name" in student)
student.update({"age": 22, "marks": 88})
print(student.pop("city"), student)
squares = {n: n * n for n in range(1, 5)}
print(squares)
# word frequency
freq = {}
for w in "to be or not to be".split():
    freq[w] = freq.get(w, 0) + 1
print(freq)
