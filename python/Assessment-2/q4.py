# Write a Python program to create a Student class with attributes name and marks (a list). Implement a method average() that returns the average marks and a method grade() that returns:

# A if average >= 90, B if average >= 75, C if average >= 50, otherwise F.

# Input: Student("Ravi", [85, 78, 92])

# Output: Ravi 85.0 B


class Student:
    def __init__(self, name, marks=[]):
        self.name = name
        self.marks = marks

    def average(self):
        self.avg = sum(self.marks) / len(self.marks)
        return self.avg

    def grade(self):
        if self.avg >= 90:
            return "A"
        elif self.avg >= 75:
            return "B"
        elif self.avg >= 50:
            return "c"
        else:
            return "F"


obj = Student("Ravi", [85, 78, 92])
print(f"{obj.name} {obj.average()} {obj.grade()}")
