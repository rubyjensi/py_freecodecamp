N = 4

# Bahar wala loop (Rows ke liye)
for i in range(N):  # i ki value hogi: 0, 1, 2, 3
    
    # Andar wala loop (Columns ke liye)
    # Is baar range me N nahi, balki (i + 1) likhenge
    for j in range(i + 1):  
        print("*", end=" ")  # Star print karo aur space do
        
    print()  # Line change karo (Enter)