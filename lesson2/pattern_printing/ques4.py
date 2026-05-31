line = '*'
max_length = 11  # Kyunki sabse beech wali line mein 11 stars hain

# PART 1: Stars ko badhane ke liye (1, 3, 5, 7, 9)
while len(line) < max_length:
    print(f"{line:^11}")  # ^11 matlab center mein rakho aur total width 11 rakho
    line += "**"          # Har baar 2 stars jodd rahe hain (Odd numbers ke liye)

# PART 2: Stars ko ghatane ke liye (11 se lekar 1 star tak)
while len(line) > 0:
    print(f"{line:^11}")  # Yahan bhi center align rahega
    line = line[:-2]      # Har baar piche se 2 stars kaat rahe hain