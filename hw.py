"""
Python Basic Programs
1. Arithmetic Operations
2. Addition using User Input
3. Swapping Variables (With & Without Third Variable)
"""

# 1 Arithmetic Operations
x = 10
y = 5

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Floor Division:", x // y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponent:", x ** y)


# 2️ Addition using User Input
# Uncomment below lines to test input

# x = int(input("Enter the 1st number: "))
# y = int(input("Enter the 2nd number: "))
# print("Addition:", x + y)


# 3️ Swap Using Third Variable
a = 10
b = 20

temp = a
a = b
b = temp

print("After swapping using third variable:")
print("First number:", a)
print("Second number:", b)


# 4️ Swap Without Third Variable
m = 89
n = 28

m, n = n, m

print("After swapping without third variable:")
print("m value:", m)
print("n value:", n)
