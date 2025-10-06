"""8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados."""

def make_shirt(size="s", message="Shirt Message"):
    print("Shirt size: " + size + ", the message: " + message)

make_shirt("large", "Python is awesome!")
make_shirt(size="extra large", message="I'm learninh Python!")
make_shirt(message="I love Python!", size="medium")