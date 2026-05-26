is_peak_hours = True
is_raining = False
has_coupon = True
result = (is_peak_hours or is_raining) and not has_coupon 
print(result)