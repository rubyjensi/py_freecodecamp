N = 4
counter = 1
for i in range(N):
    for j in range(i + 1):
        print(counter, end=" ")
        counter = counter + 1

    print()
