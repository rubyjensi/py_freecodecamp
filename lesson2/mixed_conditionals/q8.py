# E-commerce Return Policy Checker
days_since_purchase = 15
is_item_damaged = False

if is_item_damaged == True:
    print("Return Status: Approved for Immediate Replacement")
elif days_since_purchase <= 30:
    print("Return Status: Approved for Refund")
else:
    print("Return Status: Rejected (30-day limit exceeded)")