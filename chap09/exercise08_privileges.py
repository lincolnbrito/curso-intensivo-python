"""9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie
uma instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios."""

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show(self):
        for privilege in self.privileges:
            print(f"{privilege}")

    def add(self, privileges=[]):
        for privilege in privileges:
            self.privileges.append(privilege)        


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
        self.privileges = Privileges([])

    def add_privileges(self, privileges=[]):
        self.privileges.add(privileges)

    def show_privileges(self):
        self.privileges.show()


adm = Admin("Lincoln", "Brito")
adm.add_privileges(["can add post", "can delete post"])
adm.show_privileges()