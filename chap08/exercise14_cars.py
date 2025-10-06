"""8.14 – Carros: Escreva uma função que armazene informações sobre um carro
em um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser
aceito. Chame a função com as informações necessárias e dois outros pares
nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
color=’blue’, tow_package=True) Mostre o dicionário devolvido para garantir
que todas as informações foram armazenadas corretamente."""

def make_car(manufacturer, model, **attributes):
    car = { "manufacturer":manufacturer, "model":model }

    for key,value in attributes.items():
        car[key] = value

    return car

car1 = make_car("subaru", "outback", color="black", turbo=True)
car2 = make_car("ford", "Ecosport", color="red", year=2025)

print(car1)
print(car2)