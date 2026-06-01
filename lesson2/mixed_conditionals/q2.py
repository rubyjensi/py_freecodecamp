order_amount = 1600
is_premium_number = True
if order_amount >= 2000 and is_premium_number == True:
    print("30% Mega Discount Applied")
elif order_amount >= 1000:
    print("10% Standard Discount Applied")
else:
    print("No Discount Applicable")