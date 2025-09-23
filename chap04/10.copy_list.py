foods = ["pizza", "falafel", "carrot cake"]

friend_foods = foods[:]

foods.append("ice cream")
print("My favorite foods:", end=None)
for my in foods:
    print("\t"+my)

print("My fried's favorite foods: ")
for friend in friend_foods:
    print("\t"+friend)