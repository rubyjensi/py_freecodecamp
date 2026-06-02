# E-Commerce Courier Login Dashboard
company_id = "DELIVERY_2026"
secret_pin = 9988

if company_id == "DELIVERY_2026":
    print("Company ID Recognized.")
    # ID sahi hai, ab security PIN check karo
    if secret_pin == 9988:
        print("Login Successful! Loading your delivery route today...")
    else:
        print("Login Failed: Incorrect Security PIN.")
else:
    print("Access Denied: Invalid Company ID.")