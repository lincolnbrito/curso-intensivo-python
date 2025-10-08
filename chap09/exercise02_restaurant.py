"""9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
instâncias diferentes da classe e chame describe_restaurant() para cada
instância."""

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe(self):
        print(f"Restaurant: {self.name} | Cuisine type: {self.cuisine_type}")

    def open(self):
        print(self.name + " is open")

restaurant1 = Restaurant("Zelo", "Contemporary")
restaurant2 = Restaurant("Arturito", "Mediterranean")
restaurant3 = Restaurant("Amado", "Mediterranean")

restaurant1.describe()
restaurant2.describe() 
restaurant3.describe()