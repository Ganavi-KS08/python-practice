"""
Python Basics Practice
Topics Covered:
- Variables & Data Types
- Input & Output
- String Operations
- Boolean & Comparison
- Tuples & Lists
- Type Conversion
"""

# String operations
msg = "hello world"
print(msg.strip())
print(msg.upper())
print(msg.lower())

name = "Ganavi"
print(len(name))
print(name[2])
print(name[2:])
print(name[-1])

# Boolean operations
a = 20
b = 70
print(a <= b)
print(True and False)
print(1 > 2 or 2 < 4)

# Tuple operations
genders = ("female", "male", "others")
print(len(genders))

tuple1 = ("no", "yes")
tuple2 = ("she", "he")
combined = tuple1 + tuple2
print(combined)

# List operations
items = ['bru', 'sugar', 'chocolate']
items.pop()
items.append("biscuits")
print(items)

# Type conversion
age = 25
s1 = str(age)
print(s1)
print(type(s1))
