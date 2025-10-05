"""7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
166mensagem informando que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de 'pastrami' e
sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
finished_sandwiches."""

sandwich_orders = ["cheese", "pastrami", "cheese egg", "pastrami", "bacon", "atum", "pastrami"]
finished_sandwichers = []

print("We're out of pastrami!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    order = sandwich_orders.pop()
    print("I just prepared your " + order + " sandwich!")
    finished_sandwichers.append(order)

print()

for sandwich in finished_sandwichers:
    print(sandwich + " sandwich finished")