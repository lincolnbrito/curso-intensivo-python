"""8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido."""

def city_country(city, country):
    return city + ", " + country

print(city_country("São Paulo", "Brazil"))
print(city_country("Santiago", "Chile"))
print(city_country("New York", "USA"))