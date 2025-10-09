"""9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva
uma classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer
versão da classe funcionará; basta escolher aquela de que você mais gosta.
Adicione um atributo chamado flavors que armazene uma lista de sabores de
sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de
IceCreamStand e chame esse método."""

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe(self):
        print(f"Restaurant: {self.name} | Cuisine type: {self.cuisine_type}")

    def open(self):
        print(self.name + " is open")


class IceCreamStand(Restaurant):
    def __init__(self, name, flavors=[]):
        super().__init__(name, "icecream")
        self.flavors = flavors
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(f"-{flavor}")

stand1 = IceCreamStand("Chiquinho", ["chocolate", "vanilla", "strawberry", "lemon", "cream"])
stand1.describe()
stand1.show_flavors()