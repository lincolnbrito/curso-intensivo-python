usernames = ["john", "ben", "vicent", "sarah"]

new_users = ["john", "sarah", "Lincoln"]

for new_user in new_users:
    if (new_user.lower() in usernames 
        or new_user.upper() in usernames
        or new_user.title() in usernames
    ):
        print("You need to use another username")
    else:
        print(new_user + " is available")    
