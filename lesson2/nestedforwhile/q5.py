# OTP Retry & Lock System (For inside For)
for attempt in range(1, 3):  
    print(f"--- Login Attempt {attempt} ---")
    for resend in range(1, 4):  
        print(f"Sending OTP code... Try number: {resend}")
    print("Attempt failed. Resetting secure connection.\n")
print("System Alert: Maximun attempts reached. Account locked for 24 hours.")