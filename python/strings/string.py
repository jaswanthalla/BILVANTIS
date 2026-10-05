s = "  Hello, Python World  "
print(s.strip())
print(s.upper(), s.lower().strip())
t = s.strip()
print(t[0], t[-1], t[0:5], t[::-1])
print(t.replace("Python", "Java"))
print(t.split(","))
print("-".join(["a", "b", "c"]))
print(t.find("Python"), t.count("o"), t.startswith("Hello"))
print("123".isdigit(), "abc".isalpha(), "Ab1".isalnum())
name, mark = "Ravi", 91.5
print(f"{name} scored {mark:.2f}")
print(len(t), "Py" in t)
print("""Multi
line""")
