foods = ["pizza", "ice cream", "cake", "rice", "carrot", "bean", "milk"]

print("The first three items on the list are:")
print(foods[:3])

print("The three items in the middle of the list are:")
middle = len(foods)//2
print(foods[middle-1:middle+2])

print("The last three items of the list are:")
print(foods[-3:])