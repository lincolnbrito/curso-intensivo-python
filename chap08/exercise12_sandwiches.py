"""8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez."""
def make_sandwiche(*toppings):
    print("\nHere are the sandwich ingredients: ")
    for topping in toppings:
        print("- " + topping)

make_sandwiche("cheese", "pepperoni", "olive")
make_sandwiche("bacon", "cheese")