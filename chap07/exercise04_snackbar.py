sandwich_orders = ["cheese", "cheese egg bacon", "atum"]

finished_sandwichers = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print("I just prepared your " + order + " sandwich!")
    finished_sandwichers.append(order)

print()

for sandwich in finished_sandwichers:
    print(sandwich + " sandwich finished")