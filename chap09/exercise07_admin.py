"""9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva uma
classe chamada Admin que herde da classe User escrita no Exercício 9.3
(página 226), ou no Exercício 9.5 (página 232). Adicione um atributo
privileges que armazene uma lista de strings como "can add post", "can
delete post" "can ban user", e assim por diante. Escreva um método chamado
show_privileges() que liste o conjunto de privilégios de um administrador. Crie
uma instância de Admin e chame seu método."""

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe(self):
        print("\nUSER DETAILS")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    def greet(self):
        print(f"Hello {self.first_name}!")

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def add_privileges(self, privileges=[]):
        for privilege in privileges:
            self.privileges.append(privilege)

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege}")


adm = Admin("Lincoln", "Brito")
adm.add_privileges(["can add post", "can delete post"])
adm.show_privileges()