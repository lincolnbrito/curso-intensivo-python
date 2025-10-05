"""7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu
sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
prontos, mostre uma mensagem que liste cada sanduíche preparado.
"""

sandwich_orders = ["cheese", "cheese egg bacon", "atum"]
finished_sandwichers = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print("I just prepared your " + order + " sandwich!")
    finished_sandwichers.append(order)

print()

for sandwich in finished_sandwichers:
    print(sandwich + " sandwich finished")