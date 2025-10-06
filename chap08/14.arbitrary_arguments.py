def make_pizza(*toppings):
    """Show the ordered ingredients"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('cheese', 'bacon', 'peperoni')
make_pizza('cheese')