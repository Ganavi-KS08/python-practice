"""
Loop Practice Programs
Topics Covered:
- Iteration of lists
- break statement
- Nested loops
- continue statement
- enumerate function
"""

# --------------------------------------------------
# 1️ Iteration of List
# --------------------------------------------------

# l = ["mysuru", "bengaluru", "udupi"]
# for city in l:
#     print(city)


# --------------------------------------------------
# 2️ Break Statement Example
# break statement - to stop iteration when the value is found
# --------------------------------------------------

# keys = [202, 12, 234, 557]
# for doorkey in keys:
#     if doorkey == 234:
#         print("doorkey found:", doorkey)
#         break
#     print(doorkey)


# --------------------------------------------------
# 3️ Nested Loops (Multiplication Table)
# --------------------------------------------------

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} * {j} =", i * j)
#     print()


# --------------------------------------------------
# 4️ Continue Statement Example
# continue statement is used to skip the current iteration
# and move on to the next one
# --------------------------------------------------

# names = ["ganavi", "ganaviks", "ganavigowda"]
# for name in names:
#     if name == "ganavi":
#         continue
#     print(name)


# --------------------------------------------------
# 5️ Enumerate Function Example
# --------------------------------------------------

places = ["zoo", "palace", "krs", "aquaworld"]

for index, place in enumerate(places):
    print(f"Place: {index + 1} : {place}")
