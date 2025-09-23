usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello " + username + " would like to see a status report?")
        else:
            print("Welcome back, "+ username)
else:
    print("We need to find some users!")