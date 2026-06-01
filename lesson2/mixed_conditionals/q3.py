units_consumed = 350
if units_consumed >= 100:
    print("Rate: $5 per unit")
elif 101 < units_consumed < 300:
    print("Rate: $8 per unit")
elif units_consumed > 300:
    print("Rate: $12 per unit")