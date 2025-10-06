"""8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
Exercício 8.9. Escreva uma função chamada make_great() que modifique a
lista de mágicos acrescentando a expressão o Grande ao nome de cada
mágico. Chame show_magicians() para ver se a lista foi realmente modificada."""
def show_magicians(magicians):
    for magician in magicians:
        print("Magician: " + magician)

def make_great(magicians):
    for magician in magicians:
       magician = "The great " + magician

magicians = ["David Blaine", "Criss Angel", "Uri Geller", "Mr. M"]

make_great(magicians)
show_magicians(magicians)