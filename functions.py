# 1. Simple function
def hello():
    print("Hello World")

hello()


# 2. Function with parameters
def add(a, b):
    return a + b

print(add(10, 20))


# 3. Subtraction
def subtract(a, b):
    return a - b

print(subtract(20, 5))


# 4. Multiplication
def multiply(a, b):
    return a * b

print(multiply(4, 5))


# 5. Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(10, 2))




# Important Python Functions

# Square of a number
def square(n):
    return n * n

print(square(5))  # 25


# Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(even_odd(7))  # Odd


# Find maximum of two numbers
def maximum(a, b):
    return max(a, b)

print(maximum(10, 20))  # 20



# Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120


# Reverse a string
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))  # nohtyP


# Check palindrome
def palindrome(text):
    return text == text[::-1]

print(palindrome("madam"))  # True