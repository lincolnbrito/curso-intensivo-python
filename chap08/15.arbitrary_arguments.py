def make_pizza(size, *toppings):
    """Present the pizza we are about to prepare"""    
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(14, 'cheese', 'bacon', 'peperoni')
make_pizza(24, 'cheese')