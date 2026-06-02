# Premium Video Streaming Access
has_subscription = True
video_age_rating = 18
user_age = 15

if has_subscription == True:
    print("Subscription verified.")
    if video_age_rating <= user_age:
        print("Streaming started. Enjoy your movie!")
    else:
        print("Content Blocked: Parental Control Active (Age limit exceeded).")
else:
    print("Access Denied: Please buy a subscription to watch.")