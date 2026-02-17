# # Multiples of 3:
# # Write a for loop that prints all multiples of 3 between 1 and 30.
for i in range(1,31):
   if i %3==0:
       print("Multiple of 3 is:",i)

# Sum of First 10 Numbers:
# Write a program using a for loop that calculates the sum of numbers from 1 to 10.
for i in range(1,11):
    print("Sum of first 10 numbers:", i[0]+i[11])


# Print Your Name Letter by Letter:
# Write a program that takes your name as input and prints each letter of your name using a for loop.

name= input("Enter your name:")
for letters in name:
    print("Each letterof my name is:" ,letters)


# Count Vowels in a String:
# Write a program that counts how many vowels are in a given string using a for loop

text = input("Enter a string\n")
vowels=['a','e','i','o','u']
count = 0
for ch in text.lower():
    if ch in vowels:
        count += 1
print(count)


# Reverse and Sort a List
list = [1,23,46,23,57]
list.sort(reverse=True)
print(list)

list.reverse()
print(list)


# Dictionary Operations
d = {
    "Bengaluru": "Dosa",
    "Mysuru": "Vada",
    "Hassan": "Roti",
    "Mangaluru": "Fish",
    "Belagavi": "Chapathi"
}

d["Mandya"] = "Rice"
d["Bengaluru"] = "Parota"
d.pop("Mysuru")

print("Cities:", d.keys())
print("Dishes:", d.values())


# Nested Dictionary Practice


dic1 = {"Name": "Ganavi", "Subject": "English", "Food": "Biryani"}
dic2 = {"Name": "Guns", "Subject": "Kannada", "Food": "Chapathi"}

print(dic1["Food"])

