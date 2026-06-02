main_gate = "Open"
has_key = True

if main_gate == "Open":
    print("Entered the bank.")
    # Yeh andar wala if tabhi chalega jab gate open hoga
    if has_key == True:
        print("Locker opened successfully!")
    else:
        print("Locker locked: Key is missing.")
else:
    print("Cannot enter: Bank is closed.")