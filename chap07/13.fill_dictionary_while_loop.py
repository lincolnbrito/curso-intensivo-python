responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is you name?")
    response = input("Which mountain would you like to climb someday?")
    # Store response on dict
    responses[name] = response

    # Ask if another person will respond the poll
    repeat = input("Would you like to let another person respond? (yes|no)")
    if repeat == "no": 
        polling_active = False

# The poll is finished. Show the results
print("\n---- Poll Results ----")

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
