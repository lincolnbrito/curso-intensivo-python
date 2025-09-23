pizzas = ["mozzarella", "pepperoni", "bacon", "korn"]

friend_pizzas = pizzas[:]

pizzas.append("portuguese")
friend_pizzas.append("chicken")

print("My favorite pizzas:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas:")
for friend in friend_pizzas:
    print(friend)
