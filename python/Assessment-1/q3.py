# 3.Write a Python program that accepts the marks of 5 subjects for each student and calculates the student's total marks, average, grade, and result.

# Requirements:

# Use a loop to accept marks for 5 subjects.

# Validate each mark:

# If marks are less than 0 or greater than 100, display "Invalid marks" and ask the user to enter the marks again.


# Calculate: Total marks, Average marks

# Determine the grade using if-elif-else:

# Average >= 90 → A

# Average >= 75 → B

# Average >= 60 → C

# Average >= 50 → D

# Below 50 → F

# The student should pass only if all subjects have marks >= 40.

# If the student fails in even one subject, display "FAIL" regardless of the average.


students = int(input("enter no of students:"))

student_record = []

for i in range(students):
    print(f"enter the marks of student {i + 1}:")
    marks = []
    for j in range(5):
        while True:
            mark = int(input(f"subject {j + 1}:"))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("invalid marks")

    total = sum(marks)
    average = total / len(marks)

    # Determine grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if all(mark >= 40 for mark in marks):
        result = "pass"

    else:
        result = "fail"

    print(f"\nStudent {i + 1} Results:")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
