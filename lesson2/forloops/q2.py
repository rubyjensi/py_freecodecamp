total = 0
for i in range(1, 5):
    total += i
print("The final sum is:", total)

# Table of 3
for i in range(1, 11):
    print(f"3 * {i} = {3 * i}")

# Character Multiplier
name = "VIT"
for char in name:
    print(char)  

# Count Specific Characters
word = "success"
count = 0
for char in word:
    if char == 's':
        count += 1
print("Total 's' characters found:", count)  

# Squares Finder
for i in range(1, 5):
    square = i ** 2
    print(f"Square of {i} is: {square}")

# Flash Alert System
for x in range(1, 4):
    print(f"Alert Zone {x}")