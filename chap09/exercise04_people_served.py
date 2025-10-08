"""9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
225). Acrescente um atributo chamado number_served cujo valor default é 0.
Crie uma instância chamada restaurant a partir dessa classe. Apresente o
número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e
exiba-o novamente.
Adicione um método chamado set_number_served() que permita definir o
número de clientes atendidos. Chame esse método com um novo número e
mostre o valor novamente.
Acrescente um método chamado increment_number_served() que permita
incrementar o número de clientes servidos. Chame esse método com qualquer
número que você quiser e que represente quantos clientes foram atendidos, por
exemplo, em um dia de funcionamento."""

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe(self):
        print(f"Restaurant: {self.name} | Cuisine type: {self.cuisine_type}")

    def open(self):
        print(self.name + " is open")

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number

restaurant1 = Restaurant("Zelo", "Contemporary")
restaurant1.number_served = 100
print(f"Restaurant {restaurant1.name} served {restaurant1.number_served} people")

# set number served by method call
restaurant1.set_number_served(200)
print(f"Restaurant {restaurant1.name} served {restaurant1.number_served} people")

# increment served
restaurant1.increment_number_served(20)
print(f"Restaurant {restaurant1.name} served {restaurant1.number_served} people")