"""9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à
sua classe User do Exercício 9.3 (página 226). Escreva um método chamado
increment_login_attempts() que incremente o valor de login_attempts em 1.
Escreva outro método chamado reset_login_attempts() que reinicie o valor de
login_attempts com 0.
Crie uma instância da classe User e chame increment_login_attempts()
várias vezes. Exiba o valor de login_attempts para garantir que ele foi
incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). Exiba login_attempts novamente para garantir que
seu valor foi reiniciado com 0."""

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe(self):
        print("\nUSER DETAILS")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    def greet(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Luke", "Skywalker")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)