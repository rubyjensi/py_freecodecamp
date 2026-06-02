# Multiplication Tables 1 to 3 (For inside For)
for num in range(1, 4):  
    print(f"--- Table of {num} ---")
    for i in range(1, 6):  
        print(f"{num} * {i} = {num * i}")
    print()  