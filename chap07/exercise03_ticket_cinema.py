prompt = "\nInform your age (-1 to quit): "
ticket_price = 0

while True:
    age = int(input(prompt))
    if age == -1:
        break
    elif age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    elif age > 12:
        ticket_price = 15
    print("\nFor " + str(age) + " $" + str(ticket_price))