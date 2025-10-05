prompt = "Inform the pizza ingredient: "
ingredient = ""

while True:
    ingredient = input(prompt)
    if ingredient == "quit":
        break
    print("\nI will add " + ingredient + " to your pizza\n")