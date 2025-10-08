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

user1 = User("Luke", "Skywalker")
user2 = User("Anakin", "Skywaler")
user3 = User("Obi-wan", "Kenobi")

user1.describe()
user2.describe()
user3.describe()

print("\nGREETING USERS:")
user1.greet()
user2.greet()
user3.greet()