"""7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
código que apresente os resultados da enquete."""

responses = []
active_poll = True

while active_poll:
    response = input("If you could visit any place in the world, where would you go?")
    responses.append(response)

    active = input("Would you like to respond the poll? (yes|no)")
    if active == "no":
        active_poll = False

print("\n---- Poll Result ----")
for response in responses:
    print(response)