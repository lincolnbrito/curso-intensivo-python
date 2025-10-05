unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

# Verifies each user until there are no more unconfirmed users
# Trasfer each confirmed user to a confirmed users list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifing user: " + current_user.title())
    confirmed_users.append(current_user)

# Show all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
