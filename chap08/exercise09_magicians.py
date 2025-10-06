"""8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da
lista."""
def show_magicians(magicians):
    for magician in magicians:
        print("Magician: " + magician)

magicians = ["David Blaine", "Criss Angel", "Uri Geller", "Mr. M"]

show_magicians(magicians)