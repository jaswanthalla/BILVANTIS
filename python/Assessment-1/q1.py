# 1. Given the following list:

# employees = [

#     {"id": 101, "name": "John", "salary": 50000},

#     {"id": 102, "name": "Alice", "salary": 70000},

#     {"id": 103, "name": "Bob", "salary": 60000}

# ]

# Perform the following operations:

# 1.Find the employee with the highest salary.

# 2.Sort employees by salary in descending order.

# 3.Create a new list containing only employee names.

employees = [
    {"id": 101, "name": "John", "salary": 50000},
    {"id": 102, "name": "Alice", "salary": 70000},
    {"id": 103, "name": "Bob", "salary": 60000},
]

highest_salary = max(employees, key=lambda emp: emp["salary"])
print(highest_salary)

descending = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
print(descending)

names = [emp["name"] for emp in employees]
print(names)
