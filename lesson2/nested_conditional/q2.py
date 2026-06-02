entered_pin = 1234
withdraw_amount = 500
balance = 10000
if entered_pin == 1234:
    if withdraw_amount <= balance:
        print("Cash dispensed!")
    else:
        print("Insufficient amount!")
else:
    print("PIN is incorrect. Card blocked.")