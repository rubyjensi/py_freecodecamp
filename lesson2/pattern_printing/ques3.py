#from the video 

line = '*'
max_length = 6  # Maximum jitne stars chahiye

# Stars ko badhane ke liye (Right align ke saath)
while len(line) < max_length:
    print(f"{line:>6}")  # >6 matlab right side chipka do aur total width 6 rakho
    line += "*"

# Stars ko ghatane ke liye (Right align ke saath)
while len(line) > 0:
    print(f"{line:>6}")  # Yahan bhi right align rahega
    line = line[:-1]
