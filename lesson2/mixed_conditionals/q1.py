# Movie Ticket Discount System
age = 25
has_coupon = True

if age < 5:
    print("Ticket: Free")
elif age >= 60:
    print("Ticket: $5 (Senior Discount)")
elif has_coupon == True:
    print("Ticket: $7 (Coupon Discount)")
else:
    print("Ticket: $10 (Regular Price)")