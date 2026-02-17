"""
Basic Python Practice:
- Variable assignment
- Type conversion
- Arithmetic operators
- Swapping variables
"""

# Variable assignment
a, b, c = 30, 50, 70
print(a, b, c)

# Data types
name = "Ganavi"
age = 20
is_student = True
print(name, age, is_student)
print(type(age))

# Type conversion
print(float(age))
print(str(age) + " " + name)

# Arithmetic operations
x = 7
y = 3
print(x + y)
print(x - y)
print(x // y)
print(x / y)
print(x * y)
print(x ** y)

# Swapping variables using temporary variable
a = 20
b = 30
temp = a
a = b
b = temp
print(a, b)


