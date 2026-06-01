# Advanced Leap Year Rules
year = 2100  # Aap is value ko badal kar check kar sakte hain

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")