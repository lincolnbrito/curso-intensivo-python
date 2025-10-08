"""9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__()
de Restaurant deve armazenar dois atributos: restaurant_name e
cuisine_type. Crie um método chamado describe_restaurant() que mostre
essas duas informações, e um método de nome open_restaurant() que exiba
uma mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os
dois atributos individualmente e, em seguida, chame os dois métodos."""

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe(self):
        print(f"Restaurant name: {self.name} | Cuisine type: {self.cuisine_type}")

    def open(self):
        print(self.name + " is open")

restaurant = Restaurant("Zelo", "Contemporary")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe()
restaurant.open()