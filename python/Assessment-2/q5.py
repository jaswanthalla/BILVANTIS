# Write a generator function fibonacci(n) that yields the first n Fibonacci numbers. Print them using a for loop.

# Input: n = 7

# Output: 0 1 1 2 3 5 8


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  # produce the next Fibonacci number
        a, b = b, a + b


n = 7
for num in fibonacci(n):
    print(num, end=" ")
