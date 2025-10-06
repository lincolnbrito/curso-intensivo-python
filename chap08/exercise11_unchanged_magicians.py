"""8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico"""
def show_magicians(magicians):
    for magician in magicians:
        print("Magician: " + magician)

def make_great(magicians):
    great_magicians = []
    while magicians:
       current = magicians.pop()
       great_magicians.append("The great " + current)
    return great_magicians

magicians = ["David Blaine", "Criss Angel", "Uri Geller", "Mr. M"]

great_magicians = make_great(magicians[:])
show_magicians(magicians)
print("\n--------Great Magicians-------------------")
show_magicians(great_magicians)