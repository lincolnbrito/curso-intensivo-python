def greet_users(names):
    """Shows a greeting message for each user on a list"""
    for name in names:
        print("Hello, " + name.title() + "!")

names = ["hannah", "margot", "cristian"]

greet_users(names)