# Digital Clock Simulator (While inside For)
for hours in range(1, 3):  
    minutes = 0  
    while minutes <= 45:  
        print(f"Clock -> {hours}:{minutes}")
        minutes += 15  
    print("----- Hour Changed -----")