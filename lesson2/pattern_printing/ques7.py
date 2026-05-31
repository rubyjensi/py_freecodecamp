N = 4

# Bahar wala loop (Rows ke liye)
for i in range(N):  # i ki value chalegi: 0, 1, 2, 3
    
    # Andar wala loop (Columns ke liye)
    for j in range(i + 1):  
        # Is baar "*" ki jagah hum (i + 1) print kar rahe hain
        print(i + 1, end=" ")  
        
    print()  # Line change karo (Enter)