"""8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente."""

def make_shirt(size="large", message="I love Python!"):
    print("Shirt size: " + size + ", the message: " + message)

# large shirt
make_shirt()
make_shirt("large")
make_shirt(size="large")

# medium shirt
make_shirt("medium")
make_shirt(size="medium")

# another shirt
make_shirt("small", message="Python is cool!")