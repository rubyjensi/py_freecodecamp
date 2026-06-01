weather_condition = "Rainy"
is_peak_hour = True
if (weather_condition == "Rainy" or weather_condition == "Snowy") and is_peak_hour == True:
    print("Surge Price: 2.0x Applied")
elif is_peak_hour == True:
    print("Surge Price: 1.3x Applied")
else:
    print("Standard Fare Applied")